"""test_reports.py:
    Test case for reports of case2
"""
__author__      = "Adel Ramezani <adramazany@gmail.com>"

import datetime
from unittest import TestCase

from pyspark import Row
from pyspark.sql import functions
from pyspark.sql.functions import col

from eurowings import config
from eurowings.reports import Reports


class TestReports(TestCase):

    def setUp(self):
        config.searches_src_path="../test/DataLake/case1/searches"
        config.visitors_src_path="../test/DataLake/case1/visitors"


    def test_case2_search_count_by_country_region(self):
        df = Reports().searchCountByCountryRegion()

        self.assertEqual( df.filter(col("date")==datetime.date(2021, 1, 27)) \
            .filter(col("country")=='nld') \
            .filter(col("region")=='dr').collect()[0][3]
                          ,1,"case2- report first row is wrong!")

        self.assertEqual( df.where("date=='2021-01-27' and country=='deu' and region=='hh'")\
            .collect()[0][3] , 5 , "case2- report second row is incorrect!")
