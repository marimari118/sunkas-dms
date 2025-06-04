from datetime import datetime

from flaskr import db


class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    telephone_number = db.Column(db.String(255), nullable=False)
    notes = db.Column(db.Text, nullable=True)
    
    created_at = db.Column(db.DateTime(timezone=True),
        default=datetime.now(),
        nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True),
        default=datetime.now(),
        onupdate=datetime.now(),
        nullable=False)

    def __repr__(self):
        return f'<Customer {self.id}: {self.name}>'
