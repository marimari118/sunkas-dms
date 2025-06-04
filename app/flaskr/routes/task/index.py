from flask import render_template, request
from flask_login import login_required

from flaskr import db
from flaskr.models.task import Task
from flaskr.routes.task import bp


@bp.route('/')
@login_required
def index():
    tasks = db.select(Task).order_by(Task.id.desc())
    page = db.paginate(tasks, per_page=10)
    return render_template('task/index.html', page=page)
