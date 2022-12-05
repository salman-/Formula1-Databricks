# Databricks notebook source
# MAGIC %run "./../helpers/configuration"

# COMMAND ----------

# MAGIC %run "./../helpers/functions"

# COMMAND ----------

FILE_NAME = "qualifying"
qualifying_df = read_csv_file(f"{RAW_FOLDER_PATH}/{FILE_NAME}.csv")
qualifying_df = make_all_columns_snake_case(qualifying_df)
qualifying_df = add_time_stamp_to_dataframe(qualifying_df, FILE_NAME)

save_dataframe_as_parquet(qualifying_df, f"{PROCESSED_FOLDER_PATH}/{FILE_NAME}")
dbutils.notebook.exit(MESSAGE_ON_NOTEBOOK_SUCCESSY)