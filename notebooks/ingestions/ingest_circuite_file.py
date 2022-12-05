# Databricks notebook source
# MAGIC %run "./../helpers/configuration"

# COMMAND ----------

# MAGIC %run "./../helpers/functions"

# COMMAND ----------

FILE_NAME = "circuits"
circuits_df = read_csv_file(f"{RAW_FOLDER_PATH}/{FILE_NAME}.csv")
circuits_df = make_all_columns_snake_case(circuits_df)
circuits_df = add_time_stamp_to_dataframe(circuits_df, "circuits")

circuits_df = (
    circuits_df.withColumnRenamed("name", "circuit_name")
    .withColumnRenamed("lat", "latitude")
    .withColumnRenamed("lng", "longitude")
    .withColumnRenamed("alt", "altitude")
    .drop("url")
)

save_dataframe_as_parquet(circuits_df, f'{PROCESSED_FOLDER_PATH}/{FILE_NAME}')
dbutils.notebook.exit(MESSAGE_TO_WHEN_COMPLETING_NOTEBOOK_SUCCESSFULLY)