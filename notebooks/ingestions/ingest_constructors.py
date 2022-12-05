# Databricks notebook source
# MAGIC %run "./../helpers/configuration"

# COMMAND ----------

# MAGIC %run "./../helpers/functions"

# COMMAND ----------

FILE_NAME = "constructors"
constructors_df = read_csv_file(f"{RAW_FOLDER_PATH}/{FILE_NAME}.csv")
constructors_df = make_all_columns_snake_case(constructors_df)
constructors_df = add_time_stamp_to_dataframe(constructors_df, "circuits")


save_dataframe_as_parquet(constructors_df, f'{PROCESSED_FOLDER_PATH}/{FILE_NAME}')
dbutils.notebook.exit(MESSAGE_ON_NOTEBOOK_SUCCESSY)