# Databricks notebook source
# MAGIC %run "./../helpers/configuration"

# COMMAND ----------

# MAGIC %run "./../helpers/functions"

# COMMAND ----------

FILE_NAME = "pit_stops"
pitstops_df = read_csv_file(f"{RAW_FOLDER_PATH}/{FILE_NAME}.csv")
pitstops_df = make_all_columns_snake_case(pitstops_df)
pitstops_df = add_time_stamp_to_dataframe(pitstops_df, FILE_NAME)

save_dataframe_as_parquet(pitstops_df, f"{PROCESSED_FOLDER_PATH}/{FILE_NAME}")
dbutils.notebook.exit(MESSAGE_ON_NOTEBOOK_SUCCESSY)