from flaskr import db
from flaskr.models.task import Task
from flaskr.models.contract import Contract
from datetime import date



def run():
    contract = Contract.query.first()
    if not contract:
        raise Exception(contract)
    
    date_now = date.today()
    date_estimated = date(date_now.year, date_now.month+1, date_now.day)

    data = [Task(
            contract_id=contract.id,
            estimated_date=date_estimated,
            has_cleaning=True,
            has_inspection=True,
        ) for i in range(30)]
    db.session.add_all(data)
    db.session.commit()
