# Databricks notebook source
# MAGIC %run "./../helpers/configuration"

# COMMAND ----------

# MAGIC %run "./../helpers/functions"

# COMMAND ----------

from pyspark.sql.functions import countDistinct

races_df = read_parquet_file(f'{PROCESSED_FOLDER_PATH}/races').filter('year = 2019')
races_df.select(countDistinct("race_id")).show()

circuits_df = read_parquet_file(f'{PROCESSED_FOLDER_PATH}/circuits')
circuits_df.select(countDistinct("circuit_name")).show()

results_df = read_parquet_file(f'{PROCESSED_FOLDER_PATH}/results')
results_df.select(countDistinct("driver_id")).show()

drivers_df = read_parquet_file(f'{PROCESSED_FOLDER_PATH}/drivers')
drivers_df.select(countDistinct("driver_id")).show()

# COMMAND ----------

drivers_df.display()

# COMMAND ----------

races_df.display()

# COMMAND ----------

from pyspark.sql.functions import sum

races_df.join(circuits_df, circuits_df.circuit_id == races_df.circuit_id).join(
    results_df, results_df.race_id == races_df.race_id
).join(drivers_df, drivers_df.driver_id == results_df.driver_id).groupby(
    "fullname"
).agg(
    sum("points"),countDistinct("races_name")
).show()

# display(race_circiut_result_df)