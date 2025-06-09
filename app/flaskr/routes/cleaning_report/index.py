from flask import render_template, request
from flask_login import login_required

from flaskr import db
from flaskr.models.cleaning_report import CleaningReport
from flaskr.routes.cleaning_report import bp


@bp.route('/')
@login_required
def index():
    reports = CleaningReport.query.order_by(CleaningReport.completed_at.desc())
    page = db.paginate(reports, per_page=10)
    return render_template('cleaning-report/index.html', page=page)
