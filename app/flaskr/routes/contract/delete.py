from flask import url_for, redirect
from flask_login import login_required

from flaskr import db
from flaskr.models.contract import Contract
from flaskr.routes.contract import bp


@bp.route('/<int:contract_id>/delete', methods=['POST'])
@login_required
def delete(contract_id):
    contract = db.get_or_404(Contract, contract_id)
    db.session.delete(contract)

    try:
        db.session.commit()
    except:
        db.session.rollback()

    return redirect(url_for('contract.index'))
