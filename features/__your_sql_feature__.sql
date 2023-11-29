-- Databricks notebook source
create widget text timestamp default "2020-12-12"

-- COMMAND ----------

select
  1 as your_id,
  timestamp(getargument("timestamp")) as timestamp,
  10 as example_sql_feature -- TODO: replace with your logic

-- COMMAND ----------

-- MAGIC %python
-- MAGIC metadata = {
-- MAGIC     "table": "features",
-- MAGIC     "category": "",
-- MAGIC     "features": {
-- MAGIC         "example_sql_feature": {
-- MAGIC             "description": "Example SQL feature",
-- MAGIC         }
-- MAGIC     }
-- MAGIC }
