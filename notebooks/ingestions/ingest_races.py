# Databricks notebook source
# MAGIC %run "./../helpers/configuration"

# COMMAND ----------

# MAGIC %run "./../helpers/functions"

# COMMAND ----------

FILE_NAME = "races"
races_df = read_csv_file(f"{RAW_FOLDER_PATH}/{FILE_NAME}.csv")
races_df = make_all_columns_snake_case(races_df)
races_df = add_time_stamp_to_dataframe(races_df, FILE_NAME)

races_df = races_df.withColumnRenamed("name", f"{FILE_NAME}_name").drop("url")

save_dataframe_as_parquet(races_df, f"{PROCESSED_FOLDER_PATH}/{FILE_NAME}")
dbutils.notebook.exit(MESSAGE_ON_NOTEBOOK_SUCCESSY)
