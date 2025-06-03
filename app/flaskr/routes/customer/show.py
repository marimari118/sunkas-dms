from flask import render_template, request
from flask_login import login_required

from flaskr import db
from flaskr.models.customer import Customer
from flaskr.routes.customer import bp


@bp.route('/<int:customer_id>', methods=['GET'])
@login_required
def show(customer_id):
    model = db.get_or_404(Customer, customer_id)
    return render_template('customer/show.html', model=model)

