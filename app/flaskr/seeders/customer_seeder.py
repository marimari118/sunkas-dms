from flaskr import db
from flaskr.models.customer import Customer
from werkzeug.security import generate_password_hash


def run():
    data = [
        Customer(
            name='株式会社インテックス',
            address='愛知県名古屋市中村区椿町21-2 第2太閤ビルディング5階',
            telephone_number='052-485-8408',
        ),
    ]
    db.session.add_all(data)
    db.session.commit()
