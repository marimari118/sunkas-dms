from flask import render_template, request
from flask_login import login_required

from flaskr import db
from flaskr.models.cleaning_report import CleaningReport
from flaskr.routes.cleaning_report import bp


@bp.route('/<int:report_id>', methods=['GET'])
@login_required
def show(report_id):
    report = db.get_or_404(CleaningReport, report_id)
    return render_template('cleaning-report/show.html', report=report)
