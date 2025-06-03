from flask import Blueprint


bp = Blueprint('customer', __name__, url_prefix='/customer')

loaded = False


if not loaded:
    loaded = True
    from flaskr.routes.customer import index
    from flaskr.routes.customer import show
    from flaskr.routes.customer import create
    from flaskr.routes.customer import edit
    from flaskr.routes.customer import delete
