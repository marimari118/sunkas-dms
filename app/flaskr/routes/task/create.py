from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
from flaskr import db
from flaskr.routes.task import bp
from flaskr.forms.task import TaskForm
from flaskr.models.task import Task
from flaskr.models.contract import Contract


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        return request_post()
    return request_fallback()


def request_post():
    form = TaskForm()
    
    if form.validate_on_submit():
        task = Task(
            contract_id=form.contract_id.data,
            estimated_date=form.estimated_date.data,
            has_cleaning=form.has_cleaning.data,
            has_inspection=form.has_inspection.data,
            notes=form.notes.data
        )
        
        db.session.add(task)

        try:
            db.session.commit()
            return redirect(url_for('task.index'))
        except:
            db.session.rollback()

    form.contract_id.choices = [(x.id, f'{x.customer.name} - {x.contract_date}') for x in Contract.query.order_by(Contract.id.desc()).all()]
    return render_template('task/create.html', form=form)

def request_fallback():
    form = TaskForm()
    form.contract_id.choices = [(x.id, f'{x.customer.name} - {x.contract_date}') for x in Contract.query.order_by(Contract.id.desc()).all()]
    return render_template('task/create.html', form=form)