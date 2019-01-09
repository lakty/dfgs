import os


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSRF_ENABLED = True
    FLASK_DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+mysqlconnector://root:root@localhost:8889/lak_db')
    DATABASE_URL = os.environ.get('CLEARDB_DATABASE_URL', 'mysql+mysqlconnector://root:root@localhost:8889/hnuvs_db')
    PORT = int(os.environ.get('PORT', '5000'))
    SECRET_KEY = os.environ.get('SECRET_KEY', 'SITE_BOMBS')



