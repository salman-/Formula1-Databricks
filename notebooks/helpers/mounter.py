# Databricks notebook source
# MAGIC %run "./configuration"

# COMMAND ----------

CLIENT_ID = dbutils.secrets.get(scope='formula1-scope',key='client-id')
CLIENT_SECRET = dbutils.secrets.get(scope='formula1-scope',key='client-secret')
TENANT_ID = dbutils.secrets.get(scope='formula1-scope',key='tenant-id')

# COMMAND ----------

CLIENT_ID = "17ceaf76-7809-4569-9e47-da224211534a"
CLIENT_SECRET = "eY98Q~qRUmNsttzzRJHYNfYIE6LEE18ORFJwIbJa"
TENANT_ID = "1f2519d6-a33d-4336-abb5-8085bcb587d6"

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": f"{CLIENT_ID}",
           "fs.azure.account.oauth2.client.secret": f"{CLIENT_SECRET}",
           "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/token"}

# COMMAND ----------

def mount_data(storage_account,container):
    dbutils.fs.mount(
        source = f"abfss://{container}@{storage_account}.dfs.core.windows.net/",
        mount_point = f"/mnt/{storage_account}/{container}",
        extra_configs = configs)

# COMMAND ----------

mount_data(STORAGE_ACCOUNT,CONTAINER_PROCESSED_DATA)
mount_data(STORAGE_ACCOUNT,CONTAINER_RAW_DATA)
#mount_data(STORAGE_ACCOUNT,CONTAINER_CONFIG_FILE)

# COMMAND ----------

#dbutils.fs.ls(f"/mnt/{STORAGE_ACCOUNT}/{CONTAINER_PROCESSED_DATA}")
#dbutils.fs.ls(f"/mnt/{STORAGE_ACCOUNT}/{CONTAINER_RAW_DATA}")

# COMMAND ----------

def unmount_data(storage_account,container):
    dbutils.fs.unmount(f"/mnt/{storage_account}/{container}")

# COMMAND ----------

#unmount_data(STORAGE_ACCOUNT,CONTAINER_PROCESSED_DATA)
#unmount_data(STORAGE_ACCOUNT,CONTAINER_RAW_DATA)
