from os import environ as env


class Config:
    SECRET_KEY = env.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{user}:{password}@{host}/{dbname}'.format(
        host=env.get('DB_HOST'),
        user=env.get('DB_USER'),
        password=env.get('DB_PASSWORD'),
        dbname=env.get('DB_DATABASE'),
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
