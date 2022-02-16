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

    def saveOrSaveAsTable(self,dfw,tablename):
        if config.spark_sql_table_prefix!="":
            dfw.save(tablename)
        else:
            dfw.saveAsTable(tablename)


    def check_config_table_exist(self):
        try:
            max_date = self.get_last_date("test")
        except Exception as ex:
            print(ex)
            init_value = str(config.init_modefied_date)
            rdd = [Row(key='searches_last_date', value=init_value)
                   ,Row(key='visitors_last_date', value=init_value)
                   ,Row(key='test_last_date', value=init_value)
                   ]
            df = spark.createDataFrame(rdd)

            dfw = df.write \
                .mode(config.write_mode) \
                .format(config.write_format)

            self.saveOrSaveAsTable(dfw,"config")

    def get_last_date(self,who):
        df = spark.sql("select value from %sconfig where key='%s_last_date'"%(config.spark_sql_table_prefix,who))
        return float(df.collect()[0][0])

    def update_max_last_date(self,who,path):
        max_modified_date = self.get_path_max_modified_date(path)
        spark.sql("update %sconfig set value='%s' where key='%s_last_date'"%(config.spark_sql_table_prefix,str(max_modified_date),who))
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

    def _load_config(self):
        pass

    def _save_config(self):
        pass


