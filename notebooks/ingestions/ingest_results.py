# Databricks notebook source
# MAGIC %run "./../helpers/configuration"

# COMMAND ----------

# MAGIC %run "./../helpers/functions"

# COMMAND ----------

FILE_NAME = "results"
results_df = read_csv_file(f"{RAW_FOLDER_PATH}/{FILE_NAME}.csv")
results_df = make_all_columns_snake_case(results_df)
results_df = add_time_stamp_to_dataframe(results_df, FILE_NAME)
results_df = results_df.drop("status_id")

save_dataframe_as_parquet(results_df, f"{PROCESSED_FOLDER_PATH}/{FILE_NAME}")
#save_and_partition_by_dataframe_as_parquet(results_df, "race_id", f"{PROCESSED_FOLDER_PATH}/{FILE_NAME}")
dbutils.notebook.exit(MESSAGE_ON_NOTEBOOK_SUCCESSY)
