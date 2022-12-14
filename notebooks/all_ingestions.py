# Databricks notebook source
#result = dbutils.notebook.run('./ingestions/ingest_circuite',0)
#result

# COMMAND ----------

#result = dbutils.notebook.run('./ingestions/ingest_constructors',0)
#result

# COMMAND ----------

#result = dbutils.notebook.run('./ingestions/ingest_driver',0)
#result

# COMMAND ----------

#result = dbutils.notebook.run('./ingestions/ingest_pitstops',0)
#result

# COMMAND ----------

#result = dbutils.notebook.run('./ingestions/ingest_results',0)
#result

# COMMAND ----------

#result = dbutils.notebook.run('./ingestions/ingest_races',0)
#result

# COMMAND ----------

#result = dbutils.notebook.run('./ingestions/ingest_lap_times',0)
#result

# COMMAND ----------

#result = dbutils.notebook.run('./ingestions/ingest_qualifying',0)
#result

# COMMAND ----------

#result = dbutils.notebook.run('./ingestions/ingest_driver_standing',0)
#result

# COMMAND ----------

#result = dbutils.notebook.run('./ingestions/ingest_constructor_standings',0)
#result

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Run the ingestion-codes in parralel

# COMMAND ----------

from multiprocessing.pool import ThreadPool

pool = ThreadPool(5)
notebooks = [
    "ingest_constructor_standings",
    "ingest_driver_standing",
    "ingest_qualifying",
    "ingest_lap_times",
    "ingest_races",
    "ingest_results",
    "ingest_pitstops",
    "ingest_driver",
    "ingest_constructors",
    "ingest_circuite",
]
pool.map(
    lambda path: dbutils.notebook.run(
        "./ingestions/" + path, timeout_seconds=60, arguments={"input-data": path}
    ),
    notebooks,
)
