"""api.py:
    Provide APIs to calling /searches and /visitors and /report/<report>
    And also to delete gathered data for testing reason.
"""
__author__      = "Adel Ramezani <adramazany@gmail.com>"


import shutil

from flask import Response
from flask_restful import Resource

from eurowings import hlpr
from eurowings.reports import Reports
from eurowings.searches import Searches
from eurowings.visitors import Visitors

class SearchesApi(Resource):
    def get(self):
        count,max_modified_date = Searches().etl()
        return {'count':count,'max_modified_date':max_modified_date}

    def delete(self):
        name = Searches().name
        shutil.rmtree(name,ignore_errors=True)
        hlpr.update_max_last_date(name,0)

class VisitorsApi(Resource):
    def get(self):
        count,max_modified_date = Visitors().etl()
        return {'count':count,'max_modified_date':max_modified_date}

    def delete(self):
        name = Visitors().name
        shutil.rmtree(name,ignore_errors=True)
        hlpr.update_max_last_date(name,0)

class ReportsApi(Resource):
    def get(self,report):
        if report=='search_count_by_country_region':
            df = Reports().searchCountByCountryRegion()
            return df.collect()
        else:
            # raise RuntimeError('report %s is incorrect!'%report)
            return Response('{"message":"report %s is incorrect!"}'%report
                            , status=404, mimetype='application/json')

