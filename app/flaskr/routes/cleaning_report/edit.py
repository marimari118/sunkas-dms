from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
from flaskr import db
from flaskr.routes.cleaning_report import bp
from flaskr.forms.cleaning_report import CleaningReportForm
from flaskr.models.cleaning_report import CleaningReport
from flaskr.models.task import Task


@bp.route('/edit/<int:report_id>', methods=['GET', 'POST'])
@login_required
def edit(report_id):
    if request.method == 'POST':
        return request_post(report_id)
    return request_fallback(report_id)


def request_post(report_id):
    report = db.get_or_404(CleaningReport, report_id)
    form = CleaningReportForm()
    form.task_id.choices = [(x.id, f'{x.contract.customer.name} - {x.contract.installation_address} - {x.estimated_date}')
        for x in Task.query.filter(Task.has_inspection).order_by(Task.estimated_date.desc()).all()]
    
    if form.validate_on_submit():
        report.apply(form)

        try:
            db.session.commit()
            return redirect(url_for('cleaning-report.index'))
        except:
            db.session.rollback()

    return render_template('cleaning-report/edit.html', form=form)


def request_fallback(report_id):
    report = db.get_or_404(CleaningReport, report_id)
    form = CleaningReportForm(obj=report)
    form.task_id.choices = [(x.id, f'{x.contract.customer.name} - {x.contract.installation_address} - {x.estimated_date}')
        for x in Task.query.filter(Task.has_inspection).order_by(Task.estimated_date.desc()).all()]
    return render_template('cleaning-report/edit.html', form=form)