from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
from flaskr import db
from flaskr.routes.task import bp
from flaskr.forms.task import TaskForm
from flaskr.models.task import Task
from flaskr.models.contract import Contract


@bp.route('/<int:task_id>/edit', methods=['GET', 'POST'])
@login_required
def edit(task_id):
    if request.method == 'POST':
        return request_post(task_id)
    return request_fallback(task_id)


def request_post(task_id):
    task = db.get_or_404(Task, task_id)
    form = TaskForm()
    form.contract_id.choices = [(x.id, f'{x.customer.name} - {x.contract_date}') for x in Contract.query.order_by(Contract.id.desc()).all()]
    
    if not form.validate_on_submit():
        return render_template('task/edit.html', form=form, task_id=task_id)

    task.contract_id = form.contract_id.data
    task.estimated_date = form.estimated_date.data
    task.has_cleaning = form.has_cleaning.data
    task.has_inspection = form.has_inspection.data
    task.notes = form.notes.data

    try:
        db.session.commit()
        return redirect(url_for('task.index'))
    except:
        db.session.rollback()

    return render_template('task/edit.html', form=form)


def request_fallback(task_id):
    task = db.get_or_404(Task, task_id)
    form = TaskForm(obj=task)
    form.contract_id.choices = [(x.id, f'{x.customer.name} - {x.contract_date}') for x in Contract.query.order_by(Contract.id.desc()).all()]
    return render_template('task/edit.html', form=form)
