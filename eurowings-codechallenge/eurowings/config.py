"""config.py:
    Provide all configuration and decisions of the how to run for application
"""
__author__      = "Adel Ramezani <adramazany@gmail.com>"

host='0.0.0.0'
port=5000

etl_scheduler_interval_minutes=10      # 0 means disable scheduler

### connect to remove hive
# hive_metastore_uris="thrift://localhost:9083"
hive_metastore_uris=None

### using apache spark storage
spark_sql_table_prefix="parquet."
# spark_sql_table_prefix=""

### using hive storage,
# spark_sql_warehouse_dir="../spark-warehouse"
spark_sql_warehouse_dir=None

### This can be a mesos:// or spark:// URL, yarn to run on YARN, and "local" to run locally with one thread, or local[N] to run locally with N threads.
master="local[*]"

### spark display name
appName="eurowings-code-challenge"

### if spark af modifiedAfter feature works correctly in all case I could use this format to finding new files, instead of that I implements my own modifiedAfter
# init_modefied_date='2000-01-01T00:00:00'
init_modefied_date=0

### source input format
read_format="json"

### source input files filter
pathGlobFilter="*.json"

### define write mode "append" is default in some test case I'll use "overwrite"
write_mode="append"

### define write format
write_format="parquet"

### source input paths, these help changing specified path in test cases
searches_src_path="./DataLake/searches"
visitors_src_path="./DataLake/visitors"


