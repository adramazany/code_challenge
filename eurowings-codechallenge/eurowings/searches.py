"""app.py:
    Provide core etl process for searches
"""
__author__      = "Adel Ramezani <adramazany@gmail.com>"

from pyspark.sql import functions
from eurowings import hlpr, config
from eurowings.helper import spark
from os.path import abspath


class Searches:
    name:str = "searches"
    df:None

    def etl(self):
        count = self._load()
        max_modified_date=0
        if count>0:
            self._cleanse()
            self._save()
            max_modified_date = self._update_config()
        return count,max_modified_date

    def _load(self):
        last_date = hlpr.get_last_date(self.name)
        newfiles = hlpr.filter_files_modified_after(config.searches_src_path,last_date)
        if len(newfiles)>0:
            self.df = spark.read \
                .format(config.read_format) \
                .option("pathGlobFilter",config.pathGlobFilter) \
                .load( newfiles )
            return self.df.count()
        return 0

    def _cleanse(self):
        df = self.df
        df=df.withColumn("date",functions.to_date("date_time","yyyy-MM-dd'T'HH:mm:ss.SSS'Z'"))

        df=df.withColumnRenamed("flight_date_outbound","flight_date_outbound_tmp")
        df=df.withColumn("flight_date_outbound",functions.to_date("flight_date_outbound_tmp"))
        df=df.drop("flight_date_outbound_tmp")

        df=df.withColumnRenamed("flight_date_inbound","flight_date_inbound_tmp")
        df=df.withColumn("flight_date_inbound",functions.to_date("flight_date_inbound_tmp"))
        df=df.drop("flight_date_inbound_tmp")

        self.df = df

    def _save(self):
        dfw = self.df.write \
            .mode(config.write_mode) \
            .format(config.write_format)
        # .partitionBy("flight_date_outbound")
        # .bucketBy(42,"visitor_id") \
        # .sortBy("date_time") \
        hlpr.saveOrSaveAsTable(dfw,self.name)

    def _update_config(self):
        max_modified_date = hlpr.get_path_max_modified_date(config.searches_src_path)
        return hlpr.update_max_last_date(self.name, max_modified_date)

