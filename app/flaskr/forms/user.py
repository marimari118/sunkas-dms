from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField, BooleanField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    """
    ユーザーのログイン用フォーム
    """
    email = EmailField(
        'メールアドレス',
        validators=[
            DataRequired(message="メールアドレスは必須項目です。"),
            Email(message="正しい形式でメールアドレスを入力してください。"),
            Length(max=255, message="メールアドレスは255文字以内で入力してください。"),
        ]
    )
    password = PasswordField(
        'パスワード',
        validators=[
            DataRequired(message="パスワードは必須項目です。"),
            Length(min=1, max=255, message="パスワードは255文字以内で入力してください。"),
        ]
    )

    verify_error = None

    submit = SubmitField('ログイン')
