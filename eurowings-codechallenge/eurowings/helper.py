"""helper.py:
    Provide common methods to help simplicity and integrity
"""
__author__      = "Adel Ramezani <adramazany@gmail.com>"

import json
import os

from pyspark import SparkConf, Row
from pyspark.sql import SparkSession

from eurowings import config

spark = SparkSession \
    .builder.appName(config.appName) \
    .master(config.master) \
    .config("spark.sql.warehouse.dir",config.spark_sql_warehouse_dir,SparkConf()) \
    .getOrCreate()


class Helper:
    last_dates_conf={"searches_last_date":0,"visitors_last_date":0}

    def __init__(self):
        self._load_config()

    def get_last_date(self,who):
        return self.last_dates_conf[who+"_last_date"]

    def _load_config(self):
        try:
            with open("last_dates.json", "r") as configfile:
                self.last_dates_conf = json.load(configfile)
                # print(self.last_dates_conf)
        except Exception as ex:
            print(ex)
            self.update_max_last_date('test',0)

    def update_max_last_date(self,who,max_modified_date):
        self.last_dates_conf[who+"_last_date"]=max_modified_date
        with open("last_dates.json", "w") as configfile:
            json.dump(self.last_dates_conf, configfile)
        return max_modified_date

    def get_path_max_modified_date(self,path):
        max_modified_date = 0
        for root, dirs, files in os.walk(path):
            max_modified_date = max(max_modified_date, max(os.stat(root+"/"+file).st_mtime for file in files) )
        return max_modified_date

    def filter_files_modified_after(self, path, modifiedAfter):
        f=[]
        for root, dirs, files in os.walk(path):
            for file in files:
                if os.stat(root+"/"+file).st_mtime>modifiedAfter:
                    f.append(root+"/"+file)
        return f

    def recreate_spark(self):
        builder = SparkSession \
            .builder.appName(config.appName) \
            .master(config.master)
        if config.hive_metastore_uris:
            builder.config("hive.metastore.uris",config.hive_metastore_uris,SparkConf())
        if config.spark_sql_warehouse_dir:
            builder.config("spark.sql.warehouse.dir",config.spark_sql_warehouse_dir,SparkConf())

        spark = builder.getOrCreate()
        return spark

    def saveOrSaveAsTable(self,dfw,tablename):
        if config.spark_sql_table_prefix!="":
            dfw.save(tablename)
        else:
            dfw.saveAsTable(tablename)


