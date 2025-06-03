from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flaskr.config import Config
from flask_wtf import CSRFProtect


db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    csrf.init_app(app)

    from flaskr.models.user import User
    from flaskr.routes import register_blueprints
    from flaskr.commands import register_commands
    from flaskr.models import load_models
    
    load_models()
    register_blueprints(app)
    register_commands(app)

    return app

