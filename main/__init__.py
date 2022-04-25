from flask_restplus import Api
from flask import Blueprint
from app.controllers.stocks_controller import api as stock_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Stocks API',
          version='1.0',
          description='API to scrape stocks values from yahoo finance.'
          )

api.add_namespace(stock_ns, path='/api')