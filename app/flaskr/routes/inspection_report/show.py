from flask import render_template, request
from flask_login import login_required

from flaskr import db
from flaskr.models.inspection_report import InspectionReport
from flaskr.routes.inspection_report import bp


@bp.route('/<int:report_id>', methods=['GET'])
@login_required
def show(report_id):
    report = db.get_or_404(InspectionReport, report_id)
    return render_template('inspection-report/show.html', report=report)
