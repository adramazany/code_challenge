from pyspark.sql import SparkSession
spark = SparkSession \
    .builder() \
    .appName("StructStreaming") \
    .master("yarn") \
    .config("hive.merge.mapfiles", "false") \
    .config("hive.merge.tezfiles", "false") \
    .config("parquet.enable.summary-metadata", "false") \
    .config("spark.sql.parquet.mergeSchema","false") \
    .config("hive.merge.smallfiles.avgsize", "160000000") \
    .enableHiveSupport() \
    .config("hive.exec.dynamic.partition", "true") \
    .config("hive.exec.dynamic.partition.mode", "nonstrict") \
    .config("spark.sql.orc.impl", "native") \
    .config("spark.sql.parquet.binaryAsString","true") \
    .config("spark.sql.parquet.writeLegacyFormat","true") \
    .getOrCreate()
# //.config(“spark.sql.streaming.checkpointLocation”, “hdfs://pp/apps/hive/warehouse/dev01_landing_initial_area.db”) \
