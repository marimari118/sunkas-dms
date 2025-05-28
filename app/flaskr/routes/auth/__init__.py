from flask import Blueprint


bp = Blueprint('auth', __name__, url_prefix='/auth')

loaded = False


if not loaded:
    loaded = True
    from flaskr.routes.auth import login
    from flaskr.routes.auth import logout
