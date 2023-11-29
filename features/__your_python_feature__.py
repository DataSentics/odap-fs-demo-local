# Databricks notebook source
dbutils.widgets.text("timestamp", "2020-12-12")

# COMMAND ----------

timestamp = dbutils.widgets.get("timestamp")

# COMMAND ----------

# TODO: replace with your logic
# notebook must contain dataframe 'df_final' which contains features
df_final = spark.sql(
    f"select 1 as your_id, timestamp('{timestamp}') as timestamp, 20 as example_py_feature"
)
# df_final.display()

# COMMAND ----------

metadata = {
    "table": "features",
    "category": "",
    "features": {
        "example_py_feature": {
            "description": "Example Python feature",
        }
    },
}
