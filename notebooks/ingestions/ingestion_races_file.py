# Databricks notebook source
# MAGIC %run "./../helpers/configuration"

# COMMAND ----------

# MAGIC %run "./../helpers/functions"

# COMMAND ----------

FILE_NAME = "races"
circuits_df = read_csv_file(f"{RAW_FOLDER_PATH}/{FILE_NAME}.csv")
circuits_df = make_all_columns_snake_case(circuits_df)
circuits_df = add_time_stamp_to_dataframe(circuits_df, FILE_NAME)

circuits_df = (
    circuits_df.withColumnRenamed("name", f"{FILE_NAME}_name")
    .withColumnRenamed("lat", "latitude")
    .withColumnRenamed("lng", "longitude")
    .withColumnRenamed("alt", "altitude")
    .drop("url")
)

save_dataframe_as_parquet(circuits_df, f'{PROCESSED_FOLDER_PATH}/{FILE_NAME}')
dbutils.notebook.exit(MESSAGE_ON_NOTEBOOK_SUCCESSY)