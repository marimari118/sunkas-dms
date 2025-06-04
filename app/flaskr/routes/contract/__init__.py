from flask import Blueprint


bp = Blueprint('contract', __name__, url_prefix='/contract')

loaded = False


if not loaded:
    loaded = True
    from flaskr.routes.contract import index
    from flaskr.routes.contract import show
    from flaskr.routes.contract import create
    from flaskr.routes.contract import edit
    from flaskr.routes.contract import delete
