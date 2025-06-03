from flask import request, render_template, url_for, flash, redirect
from flask_login import login_required

from flaskr import db
from flaskr.models.customer import Customer
from flaskr.forms.customer import CustomerForm
from flaskr.routes.customer import bp


@bp.route('/<int:customer_id>/edit', methods=['GET', 'POST'])
@login_required
def edit(customer_id):
    if request.method == 'POST':
        return request_post(customer_id)
    return request_fallback(customer_id)


def request_post(customer_id):
    model = db.get_or_404(Customer, customer_id)
    form = CustomerForm()
    if not form.validate_on_submit():
        return render_template('customer/edit.html', form=form, customer_id=customer_id)
    
    model.name = form.name.data
    model.address = form.address.data
    model.telephone_number = form.telephone_number.data

    try:
        db.session.commit()
        return redirect(url_for('customer.index'))
    except:
        db.session.rollback()

    return render_template('customer/edit.html', form=form)


@login_required
def request_fallback(customer_id):
    customer = db.get_or_404(Customer, customer_id)
    form = CustomerForm(obj=customer)
    return render_template('customer/edit.html', form=form, customer_id=customer_id)
