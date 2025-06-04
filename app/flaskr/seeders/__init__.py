from flaskr.seeders import user_seeder
from flaskr.seeders import customer_seeder
from flaskr.seeders import contract_seeder
from flaskr.seeders import task_seeder


def run():
    user_seeder.run()
    customer_seeder.run()
    contract_seeder.run()
    task_seeder.run()
