from flask import render_template, request, redirect, url_for
from flask_login import login_required

from flaskr import db
from flaskr.routes.customer import bp
from flaskr.forms.customer import CustomerForm
from flaskr.models.customer import Customer


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        return request_post()
    return request_fallback()


def request_post():
    form = CustomerForm()
    if not form.validate_on_submit():
        return render_template('customer/create.html', form=form)

    customer = Customer(
        name=form.name.data,
        address=form.address.data,
        telephone_number=form.telephone_number.data,
        notes=form.notes.data)
    db.session.add(customer)

    try:
        db.session.commit()
        return redirect(url_for('customer.index'))
    except:
        db.session.rollback()

    return render_template('customer/create.html', form=form)


def request_fallback():
    form = CustomerForm()
    return render_template('customer/create.html', form=form)
