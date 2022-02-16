#%%

# https://spark.apache.org/docs/latest/sql-getting-started.html

# Starting Point: SparkSession
# __requires__="pyspark==3.1.2"
# import pkg_resources
# pkg_resources.require("pyspark==3.1.2")
import pyspark
from pyspark.sql import SparkSession
spark = SparkSession \
    .builder \
    .appName("test python spark") \
    .getOrCreate()

print("spark.version=",spark.version)
print("pyspark.version=",pyspark.version.__version__)

#%%

# Creating DataFrames
df = spark.read.json("D:/workspace/code_challenge/datalake/people.json")
df.show()

#%%

## Untyped Dataset Operations (aka DataFrame Operations)

# Print the schema in a tree format
df.printSchema()

# Select only the "name" column
df.select("name").show()

# Select everybody, but increment the age by 1
df.select(df["name"],df["age"]+1).show()

# Select people older than 21
df.filter(df["age"]>21).show()

# Count people by age
df.groupby("age").count().show()


#%%

## Running SQL Queries Programmatically

# Register the DataFrame as a SQL temporary view
df.createOrReplaceTempView("people")

sql_df = spark.sql("select * from people")
sql_df.show()

#%%

## Global Temporary View

# Register the DataFrame as a global temporary view
df.createOrReplaceGlobalTempView("people")
# Global temporary view is tied to a system preserved database `global_temp`
spark.sql("select * from global_temp.people").show()

# Global temporary view is cross-session
spark.newSession().sql("select * from global_temp.people").show()


#%%

## Creating Datasets

# Datasets are similar to RDDs, however, instead of using Java serialization or Kryo
# they use a specialized Encoder to serialize the objects for processing or transmitting
# over the network. While both encoders and standard serialization are responsible
# for turning an object into bytes, encoders are code generated dynamically
# and use a format that allows Spark to perform many operations like filtering, sorting
# and hashing without deserializing the bytes back into an object.
# SCALA/JAVA


#%%

## Interoperating with RDDs

## Inferring the Schema Using Reflection

from pyspark.sql import Row
sc = spark.sparkContext
# Load a text file and convert each line to a Row.
lines = sc.textFile("D:/workspace/code_challenge/datalake/people.txt")
# parts = lines.map(lambda l: l.split(","))
# people = parts.map(lambda p:Row(name=p[0],age=int(p[1])))
parts = lines.map(lambda l: l.split(","))
people = parts.map(lambda p: Row(name=p[0], age=(int(p[1]) if len(p[1])>0 else None)))

# Infer the schema, and register the DataFrame as a table.
df_people = spark.createDataFrame(people)
# EX: Caused by: org.apache.spark.SparkException: Python worker failed to connect back.
# ANS : set PYSPARK_PYTHON=python

df_people.createOrReplaceTempView("people")

# SQL can be run over DataFrames that have been registered as a table.
kids = spark.sql("select * from people where age<10 and age>3")

# The results of SQL queries are Dataframe objects.
# rdd returns the content as an :class:`pyspark.RDD` of :class:`Row`.
kidNames = kids.rdd.map(lambda k: "name:"+k.name).collect()
for name in kidNames:
    print(name)

