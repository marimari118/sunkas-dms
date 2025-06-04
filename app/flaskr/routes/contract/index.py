from flask import render_template, request
from flask_login import login_required

from flaskr import db
from flaskr.models.contract import Contract
from flaskr.routes.contract import bp


@bp.route('/')
@login_required
def index():
    contracts = db.select(Contract).order_by(Contract.id.desc())
    page = db.paginate(contracts, per_page=10)
    return render_template('contract/index.html', page=page)
