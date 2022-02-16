"""test_visitors.py:
    Test all possible state in visitors by providing 2 case (case1,case2) data
"""
__author__      = "Adel Ramezani <adramazany@gmail.com>"

import shutil
from unittest import TestCase

from eurowings import config, hlpr
from eurowings.helper import spark
from eurowings.visitors import Visitors

class TestVisitors(TestCase):

    def setUp(self) :
        config.searches_src_path="../test/DataLake/case1/searches"
        config.visitors_src_path="../test/DataLake/case1/visitors"

    def test_case1_etl_first_time(self):
        name = Visitors().name
        shutil.rmtree(name,ignore_errors=True)
        hlpr.update_max_last_date(name,0)
        count,max_modified_date = Visitors().etl()
        self.assertEqual(9999,count,"case1 visitors loaded data is incorrect!")
        self.assertEqual(1621953315.0,max_modified_date,"case1 visitors loaded max_modified_date is incorrect!")
        # print(count,max_modified_date)

    def test_case1_loaded_count(self):
        df = spark.sql("select count(*) from parquet.visitors")
        self.assertEqual(9999,df.collect()[0][0],"wrong number of case1 visitors!")

    def test_case1_second_etl_should_zero(self):
        count,max_modified_date = Visitors().etl()
        self.assertEqual(0,count,"case1 visitors second time etl count should be zero!")

    def test_case2_etl_just_load_newfile(self):
        config.visitors_src_path="../test/DataLake/case2/visitors"
        count,max_modified_date = Visitors().etl()
        self.assertIn(count,[19998,0] ,"case2 visitors loaded count incorrect!")
        self.assertIn(max_modified_date,[1644902072.6989326,0],"case2 visitors loaded max_modified_date is incorrect ")
        # print(count,max_modified_date)

    def test_case2_loaded_count(self):
        df = spark.sql("select count(*) from parquet.visitors")
        self.assertEqual(29997,df.collect()[0][0],"wrong number of case2 visitors!")

    def test_case2_second_etl_should_zero(self):
        config.visitors_src_path="../test/DataLake/case2/visitors"
        count,max_modified_date = Visitors().etl()
        self.assertEqual(count,0,"case2 visitors second time etl count should be zero!")
