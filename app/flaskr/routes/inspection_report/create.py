from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
from flaskr import db
from flaskr.routes.inspection_report import bp
from flaskr.forms.inspection_report import InspectionReportForm
from flaskr.models.inspection_report import InspectionReport
from flaskr.models.task import Task


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        return request_post()
    return request_fallback()


def request_post():
    form = InspectionReportForm()
    form.task_id.choices = [(x.id, f'{x.contract.customer.name} - {x.contract.installation_address} - {x.estimated_date}')
        for x in Task.query.filter(Task.has_inspection).order_by(Task.estimated_date.desc()).all()]
    
    if form.validate_on_submit():
        report = InspectionReport.form(form)
        db.session.add(report)

        try:
            db.session.commit()
            return redirect(url_for('inspection-report.index'))
        except:
            db.session.rollback()

    return render_template('inspection-report/create.html', form=form)


def request_fallback():
    form = InspectionReportForm()
    form.task_id.choices = [(x.id, f'{x.contract.customer.name} - {x.contract.installation_address} - {x.estimated_date}')
        for x in Task.query.filter(Task.has_inspection).order_by(Task.estimated_date.desc()).all()]
    return render_template('inspection-report/create.html', form=form)