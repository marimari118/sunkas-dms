from flask_wtf import FlaskForm
from wtforms import TextAreaField, FloatField, SubmitField, SelectField
from wtforms.fields import DateTimeLocalField
from wtforms.validators import DataRequired, Optional, NumberRange


class CleaningReportForm(FlaskForm):
    task_id = SelectField(
        '作業予定',
        coerce=int,
        validators=[DataRequired(message="作業予定は必須項目です。")],
        description="作業予定を選択してください。"
    )
    
    completed_at = DateTimeLocalField(
        '実施日時', validators=[DataRequired()], format='%Y-%m-%dT%H:%M')

    capacity = FloatField('容量 (浄化槽の実効容量)', validators=[
        Optional(), NumberRange(min=0)])
    extraction_volume = FloatField('引抜量 (清掃時の引抜量)', validators=[
        Optional(), NumberRange(min=0)])

    notes = TextAreaField('特記事項 (管理者への伝達事項)', validators=[Optional()])

    submit = SubmitField('保存')

    def __init__(self, *args, **kwargs):
        super(CleaningReportForm, self).__init__(*args, **kwargs)
        self.task_id.choices = []
