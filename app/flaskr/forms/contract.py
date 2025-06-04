from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, DateField, SelectField
from wtforms.validators import DataRequired, Optional, Length


class ContractForm(FlaskForm):
    """
    契約情報の登録・編集用フォーム
    """
    customer_id = SelectField(
        '顧客名',
        coerce=int,
        validators=[DataRequired(message="顧客は必須項目です。")],
        description="契約対象の顧客を選択してください。"
    )
    contract_date = DateField(
        '契約日',
        validators=[Optional()],
        format='%Y-%m-%d',
        description="契約を締結した日付を入力してください。"
    )
    renewal_date = DateField(
        '更新日',
        validators=[Optional()],
        format='%Y-%m-%d',
        description="次回の契約更新日を入力してください。"
    )
    installation_address = StringField(
        '設置住所',
        validators=[Optional(), Length(
            max=255, message="設置場所住所は255文字以内で入力してください。")],
        render_kw={"placeholder": "例: 顧客住所と同じ場合は入力不要"},
        description="浄化槽の設置場所の住所を入力してください。顧客住所と異なる場合に指定します。"
    )
    septic_tank_treatment_method = StringField(
        '浄化槽処理方式',
        validators=[Optional(), Length(
            max=50, message="処理方式は50文字以内で入力してください。")],
        render_kw={"placeholder": "例: 合併処理"},
        description="浄化槽の処理方式を入力してください（例: 合併、単独）。"
    )
    septic_tank_capacity = IntegerField(
        '浄化槽容量 (人槽)',
        validators=[Optional()],
        render_kw={"placeholder": "例: 5"},
        description="浄化槽の容量（人槽）を数値で入力してください。"
    )
    notes = TextAreaField(
        '備考',
        validators=[Optional()],
        render_kw={"rows": 4, "placeholder": "契約に関する特記事項などがあれば入力してください。"},
        description="契約に関する備考や特記事項を入力します。"
    )
    submit = SubmitField('保存')

    def __init__(self, *args, **kwargs):
        super(ContractForm, self).__init__(*args, **kwargs)
        self.customer_id.choices = []
