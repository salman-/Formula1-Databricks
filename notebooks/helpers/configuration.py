# Databricks notebook source
#display(dbutils.fs.mounts())

# COMMAND ----------

RAW_FOLDER_PATH = 'dbfs:/mnt/formuleinsstorage/rawdata/unziped/'
PROCESSED_FOLDER_PATH = 'dbfs:/mnt/formuleinsstorage/processeddata'
MESSAGE_TO_WHEN_COMPLETING_NOTEBOOK_SUCCESSFULLY = 'Success'