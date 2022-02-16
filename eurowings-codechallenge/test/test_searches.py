"""test_searches.py:
    Test all possible state in searches by providing 2 case (case1,case2) data
"""
__author__      = "Adel Ramezani <adramazany@gmail.com>"

import shutil
from unittest import TestCase

from eurowings import config, hlpr
from eurowings.helper import spark
from eurowings.searches import Searches


class TestSearches(TestCase):

    def setUp(self) :
        config.searches_src_path="../test/DataLake/case1/searches"
        config.visitors_src_path="../test/DataLake/case1/visitors"

    def test_case1_etl_first_time(self):
        name = Searches().name
        shutil.rmtree(name,ignore_errors=True)
        hlpr.update_max_last_date(name,0)
        count,max_modified_date = Searches().etl()
        self.assertEqual(count,13195,"case1 loaded count should be 13195, but it is %s"%(count))
        self.assertEqual(max_modified_date,1621956481.0,"case1 loaded max_modified_date should be 1621956481.0, but it is %s"%(max_modified_date))
        # print(count,max_modified_date)

    def test_case1_loaded_count(self):
        df = spark.sql("select count(*) from parquet.searches")
        self.assertEqual(13195,df.collect()[0][0],"wrong number of case1 searches!")

    def test_case1_second_etl_should_zero(self):
        count,max_modified_date = Searches().etl()
        self.assertEqual(count,0,"case1 second time etl count should be zero!")

    def test_case2_etl_just_load_newfile(self):
        config.searches_src_path="../test/DataLake/case2/searches"
        count,max_modified_date = Searches().etl()
        self.assertIn(count,[13195,0] ,"case2 loaded count incorrect!")
        self.assertIn(max_modified_date,[1644902052.0446258,0],"case2 loaded max_modified_date is incorrect ")
        print(count,max_modified_date)

    def test_case2_loaded_count(self):
        df = spark.sql("select count(*) from parquet.searches")
        self.assertEqual(26390,df.collect()[0][0],"wrong number of case2 searches!")

    def test_case2_second_etl_should_zero(self):
        config.searches_src_path="../test/DataLake/case2/searches"
        count,max_modified_date = Searches().etl()
        self.assertEqual(count,0,"case2 second time etl count should be zero!")
