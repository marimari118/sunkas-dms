from flask import redirect, url_for
from flask_login import login_required
from flaskr import db
from flaskr.routes.inspection_report import bp
from flaskr.models.inspection_report import InspectionReport


@bp.route('/<int:report_id>/delete', methods=['POST'])
@login_required
def delete(report_id):
    report = db.get_or_404(InspectionReport, report_id)
    db.session.delete(report)

    try:
        db.session.commit()
    except:
        db.session.rollback()

    return redirect(url_for('inspection-report.index'))
