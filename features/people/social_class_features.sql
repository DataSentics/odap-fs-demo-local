-- Databricks notebook source
-- MAGIC %md
-- MAGIC
-- MAGIC ## Social class feature

-- COMMAND ----------

create widget text timestamp default "2020-12-12"

-- COMMAND ----------

select
  id as person_id,
  timestamp(getargument("timestamp")) as timestamp,
  case
    when salary <  62000 then "lower"
    when salary <  93000 then "middle"
    else "upper"
  end as social_status
from dev.odap_demo_nn.people

-- COMMAND ----------

-- MAGIC %python
-- MAGIC metadata = {
-- MAGIC     "table": "features",
-- MAGIC     "category": "",
-- MAGIC     "features": {
-- MAGIC         "social_status": {
-- MAGIC             "description": "Social class of a person",
-- MAGIC         }
-- MAGIC     }
-- MAGIC }
