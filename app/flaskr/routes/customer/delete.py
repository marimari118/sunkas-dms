from flask import url_for, redirect
from flask_login import login_required

from flaskr import db
from flaskr.models.customer import Customer
from flaskr.routes.customer import bp


@bp.route('/<int:customer_id>/delete', methods=['POST'])
@login_required
def delete(customer_id):
    customer = db.get_or_404(Customer, customer_id)
    db.session.delete(customer)

    try:
        db.session.commit()
    except:
        db.session.rollback()

    return redirect(url_for('customer.index'))
