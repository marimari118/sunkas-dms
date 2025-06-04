from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
from flaskr import db
from flaskr.routes.contract import bp
from flaskr.forms.contract import ContractForm
from flaskr.models.contract import Contract
from flaskr.models.customer import Customer


@bp.route('/<int:contract_id>/edit', methods=['GET', 'POST'])
@login_required
def edit(contract_id):
    if request.method == 'POST':
        return request_post(contract_id)
    return request_fallback(contract_id)


def request_post(contract_id):
    contract = db.get_or_404(Contract, contract_id)
    form = ContractForm()
    form.customer_id.choices = [(x.id, x.name) for x in Customer.query.order_by(Customer.name).all()]
    
    if not form.validate_on_submit():
        return render_template('contract/edit.html', form=form, contract_id=contract_id)

    contract.customer_id = form.customer_id.data
    contract.contract_date = form.contract_date.data
    contract.renewal_date = form.renewal_date.data
    contract.installation_address = form.installation_address.data
    contract.septic_tank_treatment_method = form.septic_tank_treatment_method.data
    contract.septic_tank_capacity = form.septic_tank_capacity.data
    contract.notes = form.notes.data

    try:
        db.session.commit()
        return redirect(url_for('contract.index'))
    except:
        db.session.rollback()

    return render_template('contract/edit.html', form=form)


def request_fallback(contract_id):
    contract = db.get_or_404(Contract, contract_id)
    form = ContractForm(obj=contract)
    form.customer_id.choices = [(x.id, x.name) for x in Customer.query.order_by(Customer.name).all()]
    return render_template('contract/edit.html', form=form)
