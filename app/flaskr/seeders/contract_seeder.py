from flaskr import db
from flaskr.models.customer import Customer
from flaskr.models.contract import Contract
from datetime import date


def run():
    customer = Customer.query.filter(Customer.name == '株式会社インテックス').first()
    if not customer:
        raise Exception(customer)
    
    date_now = date.today()
    date_contract = date(date_now.year, date_now.month, 1)
    date_renewal = date(date_contract.year+1,date_contract.month, date_contract.day)

    data = [
        Contract(
            customer_id=customer.id,
            contract_date=date_contract,
            renewal_date=date_renewal,
            installation_address='愛知県名古屋市中村区椿町21-2 第2太閤ビルディング5階',
            septic_tank_treatment_method='全ばっ気方式',
            septic_tank_capacity=5,
        ),
    ]
    db.session.add_all(data)
    db.session.commit()
