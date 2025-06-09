from flask import Blueprint


bp = Blueprint('cleaning-report', __name__, url_prefix='/cleaning-report')

loaded = False


if not loaded:
    loaded = True
    from flaskr.routes.cleaning_report import index
    from flaskr.routes.cleaning_report import show
    from flaskr.routes.cleaning_report import create
    from flaskr.routes.cleaning_report import edit
    from flaskr.routes.cleaning_report import delete
