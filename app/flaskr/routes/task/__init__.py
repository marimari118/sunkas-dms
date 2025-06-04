from flask import Blueprint


bp = Blueprint('task', __name__, url_prefix='/task')

loaded = False


if not loaded:
    loaded = True
    from flaskr.routes.task import index
    from flaskr.routes.task import show
    from flaskr.routes.task import create
    from flaskr.routes.task import edit
    from flaskr.routes.task import delete
