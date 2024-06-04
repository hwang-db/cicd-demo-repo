# Databricks notebook source
dbutils.widgets.text("catalog","")
dbutils.widgets.text("schema","")

# COMMAND ----------

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")

# COMMAND ----------

from pyspark.sql.types import StructType,StructField, StringType

dept = [("Finance",10), 
        ("Marketing",20), 
        ("Sales",30), 
        ("IT",40) 
      ]

deptColumns = ["dept_name","dept_id"]
deptDF = spark.createDataFrame(data=dept, schema = deptColumns)
deptDF.printSchema()
deptDF.show(truncate=False)

# COMMAND ----------

deptDF.write.mode("overwrite").saveAsTable("{0}.{1}.test_table".format(catalog, schema))

# COMMAND ----------


