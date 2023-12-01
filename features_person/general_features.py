# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC ## General features

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

# MAGIC %md
# MAGIC
# MAGIC ## Read data

# COMMAND ----------

df_people = spark.read.table("fs_demo_data.people")

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ## Feature logic

# COMMAND ----------

# real SSN validity check if needed
def _check_ssn(ssn: str):
    return (
        len(ssn) == 11
        and ssn[0:3].isdigit()
        and ssn[3] == "-"
        and ssn[4:6].isdigit()
        and ssn[6] == "-"
        and ssn[7:].isdigit()
    )

# COMMAND ----------

@F.pandas_udf(T.BooleanType())
def is_ssn_valid(s: pd.Series) -> pd.Series:
    return s.apply(lambda x: True)

# COMMAND ----------

def get_age(day_of_birth, format="yyyy-MM-dd"):
    return F.floor(
        F.datediff(F.current_date(), F.to_date(day_of_birth, format=format)) / 365.25
    )

# COMMAND ----------

df_people_features = df_people.withColumn("ssn_valid", is_ssn_valid("ssn")).withColumn(
    "age", get_age("birth_date")
)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Output

# COMMAND ----------

metadata = {
    "table": "features",
    "category": "general",
    "features": {
        "ssn_valid": {
            "description": "Whether the SSN is valid or not",
        },
        "age": {
            "description": "Age of the person in years",
        }
    },
}

# COMMAND ----------

df_final = df_people_features.select(
    F.col("id").alias("person_id"),
    F.lit(dbutils.widgets.get("timestamp")).cast("timestamp").alias("timestamp"),
    "ssn_valid",
    "age",
)
