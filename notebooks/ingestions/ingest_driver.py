# Databricks notebook source
# MAGIC %run "./../helpers/configuration"

# COMMAND ----------

# MAGIC %run "./../helpers/functions"

# COMMAND ----------

from pyspark.sql.functions import col, lit, concat

FILE_NAME = "drivers"
drivers_df = read_csv_file(f"{RAW_FOLDER_PATH}/{FILE_NAME}.csv")
drivers_df = make_all_columns_snake_case(drivers_df)
drivers_df = add_time_stamp_to_dataframe(drivers_df, FILE_NAME)
drivers_df = (
    drivers_df.withColumn("fullname", concat(col("forename"), lit(" "), col("surname")))
    .drop("forename")
    .drop("surname")
    .drop("url")
)

save_and_partition_by_dataframe_as_parquet(
    drivers_df, "driver_id", f"{PROCESSED_FOLDER_PATH}/{FILE_NAME}"
)
dbutils.notebook.exit(MESSAGE_ON_NOTEBOOK_SUCCESSY)