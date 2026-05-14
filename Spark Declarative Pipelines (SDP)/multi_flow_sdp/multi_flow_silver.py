from pyspark import pipelines as dp
from pyspark.sql.functions import *
from pyspark.sql.types import *


constraints ={
    "qty_valid": "qty >= 0",
  "total_amount_valid":"total_amount >= 0"
}

@dp.table(cluster_by_auto=True, name="multi_flow_2_silver.orders_silver_flows_demo", comment="Clean and standardize data from the multiple-flow bronze table")
@dp.expect_or_fail("timestamp_not_null", "order_timestamp IS NOT NULL")
@dp.expect_all_or_drop(constraints)
def orders_silver_flows_demo():
  return dp.read_stream("multi_flow_1_bronze.orders_bronze_flows_demo")\
      .withColumn('category', upper(col('category')))\
      .drop('file_name')



