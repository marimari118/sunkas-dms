from datetime import datetime
from flaskr import db


class Contract(db.Model):
    __tablename__ = 'contracts'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer,
        db.ForeignKey('customers.id'), nullable=False)

    contract_date = db.Column(db.Date, nullable=True)
    renewal_date = db.Column(db.Date, nullable=True)
    installation_address = db.Column(db.String(255), nullable=True)
    septic_tank_treatment_method = db.Column(db.String(50), nullable=True)
    septic_tank_capacity = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)

    created_at = db.Column(db.DateTime(timezone=True),
        default=datetime.now(),
        nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True),
        default=datetime.now(),
        onupdate=datetime.now(),
        nullable=False)

    customer = db.relationship('Customer',
        backref=db.backref('contracts', lazy='dynamic'))

    def __repr__(self):
        return f'<Contract {self.id} - {self.customer.name}>'
