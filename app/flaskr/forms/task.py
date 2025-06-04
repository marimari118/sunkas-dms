# app/flaskr/forms/task.py
from flask_wtf import FlaskForm
from wtforms import DateField, BooleanField, TextAreaField, SubmitField, HiddenField, SelectField
from wtforms.validators import DataRequired, Optional

class TaskForm(FlaskForm):
    """
    作業タスク情報の登録・編集用フォーム
    """
    contract_id = SelectField(
        '契約',
        coerce=int,
        validators=[DataRequired(message="関連する契約を選択してください。")]
    )

    estimated_date = DateField(
        '作業予定日',
        validators=[DataRequired(message="作業予定日は必須です。")],
        format='%Y-%m-%d',
        description="作業を実施する予定の日付を選択してください。"
    )
    has_cleaning = BooleanField(
        '清掃',
        default=False,
        description="このタスクに清掃作業が含まれる場合はチェックしてください。"
    )
    has_inspection = BooleanField(
        '点検',
        default=False,
        description="このタスクに点検作業が含まれる場合はチェックしてください。"
    )
    notes = TextAreaField(
        '備考',
        validators=[Optional()],
        render_kw={"rows": 3, "placeholder": "作業に関する特記事項などがあれば入力してください。"},
        description="作業タスクに関する備考を入力します。"
    )
    
    submit = SubmitField('保存')

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.contract_id.choices = []