from flask import url_for, redirect
from flask_login import login_required

from flaskr import db
from flaskr.models.task import Task
from flaskr.routes.task import bp


@bp.route('/<int:task_id>/delete', methods=['POST'])
@login_required
def delete(task_id):
    task = db.get_or_404(Task, task_id)
    db.session.delete(task)

    try:
        db.session.commit()
    except:
        db.session.rollback()

    return redirect(url_for('task.index'))
