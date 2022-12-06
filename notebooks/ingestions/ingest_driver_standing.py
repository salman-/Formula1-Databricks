# Databricks notebook source
# MAGIC %run "./../helpers/configuration"

# COMMAND ----------

# MAGIC %run "./../helpers/functions"

# COMMAND ----------

FILE_NAME = "driver_standings"
driver_standing_df = read_csv_file(f"{RAW_FOLDER_PATH}/{FILE_NAME}.csv")
driver_standing_df = make_all_columns_snake_case(driver_standing_df)
driver_standing_df = add_time_stamp_to_dataframe(driver_standing_df, FILE_NAME)

save_dataframe_as_parquet(driver_standing_df, f"{PROCESSED_FOLDER_PATH}/{FILE_NAME}")
dbutils.notebook.exit(MESSAGE_ON_NOTEBOOK_SUCCESSY)