# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Init source tables
# MAGIC
# MAGIC This notebook prepares a dummy datasets & saves them to a separate DB as tables. 

# COMMAND ----------

import pyspark.sql.functions as F
import pyspark.sql.types as T

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Settings

# COMMAND ----------

N_ROWS_PEOPLE = 10_000
N_ROWS_BIKES = 10_000 

# COMMAND ----------

CATALOG = "dev"
DB = "odap_demo_nn"

TABLE_POEPLE = "people"
TABLE_BIKES = "bike_stations"

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Load data

# COMMAND ----------

PATH_PEOPLE = "dbfs:/databricks-datasets/learning-spark-v2/people/people-10m.delta/"

df_people = spark.read.format("delta").load(PATH_PEOPLE).limit(N_ROWS_PEOPLE)

df_people.display()

# COMMAND ----------

PATH_BIKES = "dbfs:/databricks-datasets/bikeSharing/data-001/hour.csv"

df_bikes = (
    spark.read.format("csv").option("header", True).load(PATH_BIKES).limit(N_ROWS_BIKES)
)

df_bikes.display()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Schema

# COMMAND ----------

df_people_cast = df_people.select(
    F.col("id").astype(T.IntegerType()),
    F.col("firstName").alias("first_name").astype(T.StringType()),
    F.col("middleName").alias("middle_name").astype(T.StringType()),
    F.col("lastName").alias("last_name").astype(T.StringType()),
    F.col("gender").astype(T.StringType()),
    F.col("birthDate").alias("birth_date").astype(T.TimestampType()),
    F.col("ssn").astype(T.StringType()),
    F.col("salary").astype(T.IntegerType()),
)

# COMMAND ----------

df_bikes_cast = df_bikes.select(
    F.col("instant").astype(T.StringType()),
    F.to_date(F.col("dteday"), "yyyy-MM-dd").alias("date"),
    F.col("season").astype(T.StringType()),
    F.col("yr").alias("year").astype(T.IntegerType()),
    F.col("mnth").alias("month").astype(T.IntegerType()),
    F.col("hr").alias("hour").astype(T.IntegerType()),
    F.col("weekday").astype(T.StringType()),
    F.col("weathersit").alias("weather_situation").astype(T.IntegerType()),
    F.col("hum").alias("humidity").astype(T.FloatType()),
    F.col("windspeed").alias("wind_speed").astype(T.FloatType()),
    F.col("casual").astype(T.IntegerType()),
    F.col("registered").astype(T.IntegerType()),
    F.col("cnt").alias("count").astype(T.IntegerType()),
)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Create tables

# COMMAND ----------

spark.sql(f"CREATE DATABASE IF NOT EXISTS {CATALOG}.{DB}")

# COMMAND ----------

table_people = f"{CATALOG}.{DB}.{TABLE_POEPLE}"

df_people_cast.write.mode("overwrite").option("overwriteSchema", True).saveAsTable(table_people)

# COMMAND ----------

table_bikes = f"{CATALOG}.{DB}.{TABLE_BIKES}"

df_bikes_cast.write.mode("overwrite").option("overwriteSchema", True).saveAsTable(table_bikes)
