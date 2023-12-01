# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC ## Usage features

# COMMAND ----------

# MAGIC %run ../../init/odap

# COMMAND ----------

import pyspark.sql.functions as F

from odap.feature_factory.imports import get_param

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Settings

# COMMAND ----------

dbutils.widgets.text("timestamp", "2023-11-25")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Reading a parameter from config:

# COMMAND ----------

required_daily = get_param("usage_params")["daily_requirement"]

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Read data

# COMMAND ----------

df_stations = spark.read.table("fs_demo_data.bike_stations").filter(
    F.col("date") == F.to_date(F.lit(dbutils.widgets.get("timestamp")))
).drop_duplicates(subset=["station_id", "date"])

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Output

# COMMAND ----------

metadata = {
    "table": "features",
    "category": "stats",
    "features": {
        "usage_{user_type}": {
            "description": "Number of types the station was used by {user_type} users",
        },
        "used_enough": {
            "description": "Flag whether the station was used enough on a given day or not",
        },
    },
}

# COMMAND ----------

df_final = df_stations.select(
    F.col("instant").alias("station_id"),
    F.lit(dbutils.widgets.get("timestamp")).cast("timestamp").alias("timestamp"),
    F.col("casual").alias("usage_casual"), 
    F.col("registered").alias("usage_registered"),
    (F.col("count") >= required_daily).alias("used_enough"),
)
