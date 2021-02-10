import os


PROTOCOL = 'https://'
SERVER = 'sht.url'


class Configuration:

    DEBUG = True
    ENV = 'development'
    SECRET_KEY = 'development key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////./temp/urls.db' if os.name != 'nt' else 'sqlite:///./temp/urls.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
