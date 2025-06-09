from flask import render_template, request
from flask_login import login_required

from flaskr import db
from flaskr.models.inspection_report import InspectionReport
from flaskr.routes.inspection_report import bp


@bp.route('/')
@login_required
def index():
    reports = InspectionReport.query.order_by(InspectionReport.completed_at.desc())
    page = db.paginate(reports, per_page=10)
    return render_template('inspection-report/index.html', page=page)
