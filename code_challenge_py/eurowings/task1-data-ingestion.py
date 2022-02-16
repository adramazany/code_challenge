from pyspark.sql import SparkSession

spark = SparkSession \
    .builder.appName("eurowings assignment for data engineer") \
    .master("local[*]") \
    .getOrCreate()

df = spark.read \
    .format("json") \
    .option("pathGlobFilter","*.json") \
    .load("/DataLake/searches/")

df.show()
