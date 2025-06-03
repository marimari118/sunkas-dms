from flask import render_template, request
from flask_login import login_required

from flaskr import db
from flaskr.models.customer import Customer
from flaskr.routes.customer import bp


@bp.route('/')
@login_required
def index():
    models = db.select(Customer).order_by(Customer.id.desc())
    page = db.paginate(models, per_page=10)
    return render_template('customer/index.html', page=page)

