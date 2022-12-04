# Databricks notebook source
display(dbutils.fs.mounts())

# COMMAND ----------

raw_folder_path = 'dbfs:/mnt/formuleinsstorage/rawdata'
processed_folder_path = 'dbfs:/mnt/formuleinsstorage/processeddata'

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /mnt/formuleinsstorage/rawdata

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /mnt/formuleinsstorage/processeddata