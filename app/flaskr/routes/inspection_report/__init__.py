from flask import Blueprint


bp = Blueprint('inspection-report', __name__, url_prefix='/inspection-report')

loaded = False


if not loaded:
    loaded = True
    from flaskr.routes.inspection_report import index
    from flaskr.routes.inspection_report import show
    from flaskr.routes.inspection_report import create
    from flaskr.routes.inspection_report import edit
    from flaskr.routes.inspection_report import delete
