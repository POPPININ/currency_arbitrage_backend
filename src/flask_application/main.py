from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
from bellmanFordSP.Arbitrage import Arbitrage

app = Flask(__name__) 
api = Api(app) 

exchange_rates_args = reqparse.RequestParser()
exchange_rates_args.add_argument("Currency Names", type=list, help="List of currency codes", location="json", required=True)
exchange_rates_args.add_argument("Exchange Rates", type=dict, help="Dictionary containing relative ER of currency", location="json", required=True)

currency_names = { }
exchange_rates = { }
currency_conversions = { }

class ExchangeRates(Resource):

    '''Get the details of an arbitrage query by its ID'''
    def get(self, ID : int):
        data = { "Currency Names" : currency_names[ID], 
                 "Exchange Rates" : exchange_rates[ID],
                 "Conversions" : currency_conversions[ID] }
        return data, 200
    

    def post(self, ID : int):
        args = exchange_rates_args.parse_args()
        currency_names[ID] = args['Currency Names']
        exchange_rates[ID] = args['Exchange Rates']
        exchRates = args['Exchange Rates']
        currencyNames = args['Currency Names']
        arbitrage = Arbitrage(exchRates=exchRates,
                              currencyNames=currencyNames)
        conversions = arbitrage.conversions
        currency_conversions[ID] = conversions 
        return { 'Conversions' : conversions }, 201

api.add_resource(ExchangeRates, '/exchangeRates/<int:ID>')
                
if __name__ == "__main__":
    app.run(debug=True)

