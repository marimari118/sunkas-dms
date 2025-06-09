from datetime import datetime
from flaskr import db
from flaskr.models.task import Task
from flaskr.forms.cleaning_report import CleaningReportForm


class CleaningReport(db.Model):
    __tablename__ = 'cleaning_reports'

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey(
        'tasks.id'), nullable=False, unique=True)
    
    completed_at = db.Column(db.DateTime, nullable=False)
    
    # 清掃内容
    capacity = db.Column(
        db.Float, nullable=True, comment='容量 (浄化槽の実効容量)')
    extraction_volume = db.Column(
        db.Float, nullable=True, comment='引抜量 (清掃時の引抜量)')

    notes = db.Column(db.Text, nullable=True,
        comment='特記事項 (管理者への伝達事項)')

    created_at = db.Column(db.DateTime,
        default=datetime.now,
        nullable=False)
    updated_at = db.Column(db.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False)

    task = db.relationship(Task,
        backref=db.backref('cleaning_report', uselist=False, cascade="all, delete-orphan"))
    
    @staticmethod
    def form(form: CleaningReportForm):
        return CleaningReport(
            task_id = form.task_id.data,
            completed_at = form.completed_at.data,
            capacity = form.capacity.data,
            extraction_volume = form.extraction_volume.data,
            notes = form.notes.data)
        
    def apply(self, form: CleaningReportForm):
        self.task_id = form.task_id.data
        self.completed_at = form.completed_at.data
        self.capacity = form.capacity.data
        self.extraction_volume = form.extraction_volume.data
        self.notes = form.notes.data

    def __repr__(self):
        return f'<CleaningReport {self.id} for Task {self.task_id}>'
