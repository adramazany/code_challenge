"""app.py:
    Provide core etl process for visitors
"""
__author__      = "Adel Ramezani <adramazany@gmail.com>"

from pyspark.sql import functions
from eurowings import hlpr, config
from eurowings.helper import spark


class Visitors:
    name:str = "visitors"
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
        newfiles = hlpr.filter_files_modified_after(config.visitors_src_path,last_date)
        if len(newfiles)>0:
            self.df = spark.read \
                .format(config.read_format) \
                .option("pathGlobFilter",config.pathGlobFilter) \
                .load( newfiles )
            return self.df.count()
        return 0

    def _cleanse(self):
        self.df=self.df.withColumn("date", functions.when(functions.length("visit_start")==19, functions.to_date("visit_start",'yyyy-MM-dd HH:mm:ss') ).otherwise(functions.to_date("visit_start",'yy-MM-dd HH:mm:ss')))

    def _save(self):
        dfw = self.df.write \
            .mode(config.write_mode) \
            .format(config.write_format)
        # .partitionBy("date")
        # .bucketBy(42,"visitor_id") \
        # .sortBy("date_time") \
        hlpr.saveOrSaveAsTable(dfw,self.name)

    def _update_config(self):
        max_modified_date = hlpr.get_path_max_modified_date(config.visitors_src_path)
        return hlpr.update_max_last_date(self.name, max_modified_date)

