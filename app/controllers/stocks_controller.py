import flask
from flask_restplus import Resource
from ..dtos.dto import StockDto
from flask import request
from flask import Response
from app.decorators.apikey import require_appkey
from app.services.stocks_service import extract_stock_history

api = StockDto.api

@api.route('/stocks/history', methods=['GET'])
class StocksHistory(Resource):
    @api.doc('Return stocks data from name of stock')
    @require_appkey
    def get(self):
        """Stock history method"""
        #content = request.json
        try:
            stock_name = request.args.get('stock_name')
            rows_limit = int(request.args.get('rows_limit'))
            response_scrape = extract_stock_history(stock_name, rows_limit)
            if response_scrape:
                response = flask.jsonify(response_scrape)
                response.headers.add('Access-Control-Allow-Origin', '*')
                return response
            else:
                return Response(status=404)
        except Exception as e:
            return Response(status=500)