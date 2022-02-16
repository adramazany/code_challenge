from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

CORS(app)

class SearchesApi(Resource):
    def get(self):
        print('accept etl searches start request.')
        return ''
    def post(self):
        print('post accept etl searches start request.')

class VisitorsApi(Resource):
    def get(self):
        print('accept etl vistors start request.')
        return ''
    def post(self):
        print('accept etl vistors start request.')

class ReportsApi(Resource):
    def get(self,report):
        if report=='search_count_by_country_region':
            return [{'date':'2021-01-27','country':'nld','region':'dr','count':1}
                    ,{'date':'2021-01-27','country':'deu','region':'hh','count':5}]
        else:
            raise RuntimeError('report %s is incorrect!'%report)

api.add_resource(SearchesApi,'/searches')
api.add_resource(VisitorsApi,'/visitors')
api.add_resource(ReportsApi,'/reports/<report>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)