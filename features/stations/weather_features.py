# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC ## Weather features

# COMMAND ----------

# MAGIC %run ../../init/odap

# COMMAND ----------

import pyspark.sql.functions as F

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Settings

# COMMAND ----------

dbutils.widgets.text("timestamp", "2023-25-11")

# COMMAND ----------

df_stations = spark.read.table("dev.odap_demo_nn.bike_stations").filter(
    F.col("date") == F.to_date(F.lit(dbutils.widgets.get("timestamp")))
).drop_duplicates(subset=["station_id", "date"])

# COMMAND ----------

metadata = {
    "table": "features",
    "category": "environment",
    "features": {
        "humidity": {
            "description": "Air humidity percentage from 0 to 1",
        },
        "wind_speed": {
            "description": "Wind speed in mps",
        },
    },
}

# COMMAND ----------

df_final = df_stations.select(
    F.col("instant").alias("station_id"),
    F.col("date").cast("timestamp").alias("timestamp"),
    "humidity", 
    "wind_speed",
)

df_final.display()
