from datetime import datetime
from flaskr import db


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    contract_id = db.Column(db.Integer, db.ForeignKey('contracts.id'), nullable=False)

    estimated_date = db.Column(db.Date, nullable=False)
    has_cleaning = db.Column(db.Boolean, nullable=False, default=False)
    has_inspection = db.Column(db.Boolean, nullable=False, default=False)
    notes = db.Column(db.Text, nullable=True)

    created_at = db.Column(db.DateTime(timezone=True),
        default=datetime.now,
        nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True),
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False)

    contract = db.relationship('Contract',
        backref=db.backref('tasks', lazy='dynamic', cascade="all, delete-orphan"))

    def __repr__(self):
        return f'<Task {self.id} on {self.estimated_date.strftime("%Y-%m-%d") if self.estimated_date else "N/A"}>'