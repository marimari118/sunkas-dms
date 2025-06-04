from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
from flaskr import db
from flaskr.routes.contract import bp
from flaskr.forms.contract import ContractForm
from flaskr.models.contract import Contract
from flaskr.models.customer import Customer


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        return request_post()
    return request_fallback()


def request_post():
    form = ContractForm()
    form.customer_id.choices = [(x.id, x.name) for x in Customer.query.order_by(Customer.name).all()]
    
    if not form.validate_on_submit():
        return render_template('contract/create.html', form=form)

    contract = Contract(
        customer_id=form.customer_id.data,
        contract_date=form.contract_date.data,
        renewal_date=form.renewal_date.data,
        installation_address=form.installation_address.data,
        septic_tank_treatment_method=form.septic_tank_treatment_method.data,
        septic_tank_capacity=form.septic_tank_capacity.data,
        notes=form.notes.data or None
    )
    db.session.add(contract)

    try:
        db.session.commit()
        return redirect(url_for('contract.index'))
    except:
        db.session.rollback()

    return render_template('contract/create.html', form=form)


def request_fallback():
    form = ContractForm()
    form.customer_id.choices = [(x.id, x.name) for x in Customer.query.order_by(Customer.name).all()]
    return render_template('contract/create.html', form=form)