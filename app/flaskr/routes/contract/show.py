from flask import render_template, request
from flask_login import login_required

from flaskr import db
from flaskr.models.contract import Contract
from flaskr.routes.contract import bp


@bp.route('/<int:contract_id>', methods=['GET'])
@login_required
def show(contract_id):
    contract = db.get_or_404(Contract, contract_id)
    return render_template('contract/show.html', contract=contract)
