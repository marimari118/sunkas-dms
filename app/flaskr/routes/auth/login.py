from flask import render_template, redirect, url_for, request
from flask_login import login_user

from flaskr.routes.auth import bp
from flaskr.models.user import User


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        verified = user and user.check_password(request.form['password'])

        if verified:
            login_user(user)
            return redirect(url_for('main.index'))

    return render_template('auth/login.html')
