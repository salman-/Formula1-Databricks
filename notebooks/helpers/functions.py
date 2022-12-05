# Databricks notebook source
import re


def camel_to_snake(name):
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


def make_all_columns_snake_case(df):
    new_column_names = []
    for col in df.columns:
        new_column_names.append(camel_to_snake(col))
    return df.toDF(*new_column_names)

# COMMAND ----------

from pyspark.sql.functions import current_timestamp


def add_time_stamp_to_dataframe(df, col_name):
    COL_POSTFIX = "_ingestion_date"
    return df.withColumn(col_name + COL_POSTFIX, current_timestamp())

# COMMAND ----------

def save_dataframe_as_parquet(df,folder_name):
    df.write.mode('overwrite').parquet(f'{processed_folder_path}/{folder_name}')

# COMMAND ----------

def read_parquet_file(path_to_parquet_file):
    return spark.read.parquet(path_to_parquet_file)

# COMMAND ----------

def read_csv_file(path_csv_file):
    return spark.read.option('header',True).option('inferSchema',True).csv(path_csv_file)