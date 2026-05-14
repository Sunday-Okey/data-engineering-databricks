from pyspark import pipelines as dp
from pyspark.sql.functions import *
from pyspark.sql.types import *

schema = StructType(
    [
        StructField("subsidiary_id", StringType(), True),
        StructField("order_id", StringType(), True),
        StructField("order_timestamp", TimestampType(), True),
        StructField("customer_id", StringType(), True),
        StructField("region", StringType(), True),
        StructField("country", StringType(), True),
        StructField("city", StringType(), True),
        StructField("channel", StringType(), True),
        StructField("sku", StringType(), True),
        StructField("category", StringType(), True),
        StructField("qty", IntegerType(), True),
        StructField("unit_price", DoubleType(), True),
        StructField("discount_pct", IntegerType(), True),
        StructField("coupon_code", StringType(), True),
        StructField("total_amount", DoubleType(), True),
        StructField("order_date", DateType(), True),
    ]
)

dp.create_streaming_table("multi_flow_1_bronze.orders_bronze_flows_demo")


@dp.append_flow(target="multi_flow_1_bronze.orders_bronze_flows_demo")
def lumina_sports_orders():
  df = spark.readStream.format("cloudFiles")\
      .option("cloudFiles.format", "csv")\
      .schema(schema)\
      .load("/Volumes/labuser15104617_1778714524/multi_flow_1_bronze/lumina_sports_orders")\
      .withColumn("file_name", col("_metadata.file_name"))
  return df


@dp.append_flow(target="multi_flow_1_bronze.orders_bronze_flows_demo")
def bright_home_orders():
  df = spark.readStream.format("cloudFiles")\
      .option("cloudFiles.format", "csv")\
      .schema(schema)\
      .load("/Volumes/labuser15104617_1778714524/multi_flow_1_bronze/bright_home_orders")\
      .withColumn("file_name", col("_metadata.file_name"))
  return df


@dp.append_flow(target="multi_flow_1_bronze.orders_bronze_flows_demo")
def northstar_outfitters_orders():
  df = spark.readStream.format("cloudFiles")\
      .option("cloudFiles.format", "json")\
      .schema(schema)\
      .load("/Volumes/labuser15104617_1778714524/multi_flow_1_bronze/northstar_outfitters_orders")\
      .withColumn("file_name", col("_metadata.file_name"))
  return df
