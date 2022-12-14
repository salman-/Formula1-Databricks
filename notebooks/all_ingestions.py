# Databricks notebook source
result = dbutils.notebook.run('./ingestions/ingest_circuite_file',0)
result

# COMMAND ----------

result = dbutils.notebook.run('./ingestions/ingest_constructors',0)
result

# COMMAND ----------

result = dbutils.notebook.run('./ingestions/ingest_driver',0)
result

# COMMAND ----------

result = dbutils.notebook.run('./ingestions/ingest_pitstops',0)
result

# COMMAND ----------

result = dbutils.notebook.run('./ingestions/ingest_results',0)
result

# COMMAND ----------

result = dbutils.notebook.run('./ingestions/ingest_races',0)
result

# COMMAND ----------

result = dbutils.notebook.run('./ingestions/ingest_lap_times',0)
result

# COMMAND ----------

result = dbutils.notebook.run('./ingestions/ingest_qualifying',0)
result

# COMMAND ----------

result = dbutils.notebook.run('./ingestions/ingest_driver_standing',0)
result

# COMMAND ----------

result = dbutils.notebook.run('./ingestions/ingest_constructor_standings',0)
result
