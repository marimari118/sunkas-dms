from flask import redirect, url_for
from flask_login import login_required
from flaskr import db
from flaskr.routes.cleaning_report import bp
from flaskr.models.cleaning_report import CleaningReport


@bp.route('/<int:report_id>/delete', methods=['POST'])
@login_required
def delete(report_id):
    report = db.get_or_404(CleaningReport, report_id)
    db.session.delete(report)

    try:
        db.session.commit()
    except:
        db.session.rollback()

    return redirect(url_for('cleaning-report.index'))
