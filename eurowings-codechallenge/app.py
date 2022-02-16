#!/usr/bin/env python

"""app.py:
    Eurowings Data Engineering Challenge Practical Assignment.
"""
__author__      = "Adel Ramezani <adramazany@gmail.com>"

from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource

from eurowings import config
from eurowings.api import SearchesApi, VisitorsApi, ReportsApi
from eurowings.scheduler import Scheduler

app = Flask(__name__)
api = Api(app)

CORS(app)

api.add_resource(SearchesApi,'/searches')
api.add_resource(VisitorsApi,'/visitors')
api.add_resource(ReportsApi,'/reports/<report>')

@app.route('/')
def welcome_page():
    return '<h1>Welcome to eurowings Data Engineering Challenge Practical Assignment</h2>'

Scheduler().start()

if __name__ == '__main__':
    # app.run(host=config.host, port=config.port, debug=True)
    app.run(debug=True)


# curl -X GET -i http://localhost:5000/searches
# curl -X DELETE -i http://localhost:5000/searches
# curl -X GET -i http://localhost:5000/visitors
# curl -X DELETE -i http://localhost:5000/visitors
# curl -X GET -i http://localhost:5000/reports/search_count_by_country_region
