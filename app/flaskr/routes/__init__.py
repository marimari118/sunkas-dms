from flaskr.routes import main
from flaskr.routes import auth


def register_blueprints(app):
    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)
