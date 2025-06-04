from flaskr.routes import main
from flaskr.routes import auth
from flaskr.routes import customer
from flaskr.routes import contract
from flaskr.routes import task


def register_blueprints(app):
    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(customer.bp)
    app.register_blueprint(contract.bp)
    app.register_blueprint(task.bp)
