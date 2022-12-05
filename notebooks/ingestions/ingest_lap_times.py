# Databricks notebook source
# MAGIC %run "./../helpers/configuration"

# COMMAND ----------

# MAGIC %run "./../helpers/functions"

# COMMAND ----------

FILE_NAME = "lap_times"
laptimes_df = read_csv_file(f"{RAW_FOLDER_PATH}/{FILE_NAME}.csv")
laptimes_df = make_all_columns_snake_case(laptimes_df)
laptimes_df = add_time_stamp_to_dataframe(laptimes_df, FILE_NAME)

save_dataframe_as_parquet(laptimes_df, f"{PROCESSED_FOLDER_PATH}/{FILE_NAME}")
dbutils.notebook.exit(MESSAGE_ON_NOTEBOOK_SUCCESSY)