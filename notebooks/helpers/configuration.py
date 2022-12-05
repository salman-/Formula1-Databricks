# Databricks notebook source
#display(dbutils.fs.mounts())

# COMMAND ----------

raw_folder_path = 'dbfs:/mnt/formuleinsstorage/rawdata/unziped/'
processed_folder_path = 'dbfs:/mnt/formuleinsstorage/processeddata'
MESSAGE_TO_WHEN_COMPLETING_NOTEBOOK_SUCCESSFULLY = 'Success'