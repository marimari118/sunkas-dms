

from flask import render_template, redirect, url_for, request
from flask_login import login_user

from flaskr.routes.auth import bp
from flaskr.models.user import User
from flaskr.forms.user import LoginForm


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return request_post()
    return request_fallback()


def request_post():
    form = LoginForm()
    if not form.validate_on_submit():
        return render_template('auth/login.html', form=form)
    
    user = User.verify(form.email.data, form.password.data)
    if not user:
        form.verify_error = 'メールアドレスまたはパスワードが正しくありません。'
        return render_template('auth/login.html', form=form)
    
    login_user(user)
    return redirect(url_for('main.index'))


def request_fallback():
    form = LoginForm()
    return render_template('auth/login.html', form=form)
