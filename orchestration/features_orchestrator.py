# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Feature Orchestration

# COMMAND ----------

# MAGIC %run ../init/odap

# COMMAND ----------

from odap.feature_factory.imports import (
    create_notebooks_widget,
    orchestrate,
    calculate_latest_table,
)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Widgets

# COMMAND ----------

# MAGIC %sql
# MAGIC create widget text timestamp default "2023-01-01"

# COMMAND ----------

create_notebooks_widget()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Orchestrate

# COMMAND ----------

orchestrate()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Calculate latest features cache

# COMMAND ----------

calculate_latest_table()
