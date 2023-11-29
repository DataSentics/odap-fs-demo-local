# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC ## Name features

# COMMAND ----------

# MAGIC %run ../../init/odap

# COMMAND ----------

import pandas as pd

import pyspark.sql.functions as F
import pyspark.sql.types as T

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Settings

# COMMAND ----------

dbutils.widgets.text("timestamp", "2023-01-01")

# COMMAND ----------

# TODO: parameters

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Read data

# COMMAND ----------

df_people = spark.read.table("dev.odap_demo_nn.people")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Output

# COMMAND ----------

metadata = {
    "table": "features",
    "category": "general",
    "features": {
        "len_{pos}_name": {
            "description": "Number of characters in person's {pos} name",
        },
    },
}

# COMMAND ----------

df_final = df_people.select(
    F.col("id").alias("person_id"),
    F.lit(dbutils.widgets.get("timestamp")).cast("timestamp").alias("timestamp"),
    *[
        F.length(col).alias(f"len_{col}")
        for col in ["first_name", "middle_name", "last_name"]
    ],
)

df_final.display()
