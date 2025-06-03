from flaskr import db
from flaskr.models.user import User
from werkzeug.security import generate_password_hash


def run():
    data = [
        User(
            username='admin',
            email='admin@example.com',
            password_hash=generate_password_hash('P@ssw0rd')
        ),
        User(
            username='user',
            email='user@example.com',
            password_hash=generate_password_hash('P@ssw0rd')
        ),
    ]
    db.session.add_all(data)
    db.session.commit()
