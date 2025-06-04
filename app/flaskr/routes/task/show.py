from flask import render_template, request
from flask_login import login_required

from flaskr import db
from flaskr.models.task import Task
from flaskr.routes.task import bp


@bp.route('/<int:task_id>', methods=['GET'])
@login_required
def show(task_id):
    task = db.get_or_404(Task, task_id)
    return render_template('task/show.html', task=task)
