import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']




class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEVELOPMENT = True
    DEBUG = True
    API_URL = 'https://stock-api-scrape.herokuapp.com'


class TestingConfig(Config):
    DEBUG = True
    #TESTING = True
    API_URL = 'https://stock-api-scrape.herokuapp.com'


class ProductionConfig(Config):
    DEBUG = False
    API_URL = 'https://stock-api-scrape.herokuapp.com'
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/'

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY