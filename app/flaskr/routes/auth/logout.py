from flask import redirect, url_for
from flask_login import logout_user, login_required

from flaskr.routes.auth import bp


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
