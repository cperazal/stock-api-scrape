from flask_restplus import Namespace, fields


class StockDto:
    api = Namespace('Stocks API', description='API to scrape stock values')