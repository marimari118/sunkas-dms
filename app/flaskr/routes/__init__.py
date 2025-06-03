from flaskr.routes import main
from flaskr.routes import auth
from flaskr.routes import customer


def register_blueprints(app):
    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(customer.bp)
