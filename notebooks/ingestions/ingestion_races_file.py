# Databricks notebook source
# MAGIC %run "./../helpers/configuration"

# COMMAND ----------

# MAGIC %run "./../helpers/functions"

# COMMAND ----------

FILE_NAME = "races"
races_df = read_csv_file(f"{RAW_FOLDER_PATH}/{FILE_NAME}.csv")
races_df = make_all_columns_snake_case(circuits_df)
races_df = add_time_stamp_to_dataframe(circuits_df, FILE_NAME)

races_df = circuits_df.withColumnRenamed("name", f"{FILE_NAME}_name").drop("url")

save_dataframe_as_parquet(circuits_df, f'{PROCESSED_FOLDER_PATH}/{FILE_NAME}')
dbutils.notebook.exit(MESSAGE_ON_NOTEBOOK_SUCCESSY)