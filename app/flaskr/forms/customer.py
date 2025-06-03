from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class CustomerForm(FlaskForm):
    """
    顧客情報の登録・編集用フォーム
    """
    name = StringField(
        '顧客名',
        validators=[
            DataRequired(message="顧客名は必須項目です。"),
            Length(min=1, max=255, message="顧客名は1～255文字で入力してください。"),
        ],
        render_kw={
            "placeholder": "例: 株式会社S様 / 田中 一郎",
        }
    )
    address = TextAreaField(
        '住所',
        validators=[
            DataRequired(message="住所は必須項目です。"),
        ],
        render_kw={
            "placeholder": "例: 東京都中央区... ビル名・部屋番号など",
            "rows": 4,
        }
    )
    telephone_number = StringField(
        '電話番号',
        validators=[
            DataRequired(message="電話番号は必須項目です。"),
            Length(min=10, max=30, message="電話番号は10～30桁で入力してください。")
        ],
        render_kw={
            "placeholder": "例: 090-1234-5678 / 03-1234-5678",
        }
    )

    submit = SubmitField('保存')
