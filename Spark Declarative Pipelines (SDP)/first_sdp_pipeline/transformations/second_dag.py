# from pyspark import pipelines as dp
# from pyspark.sql.functions import *

# # Materialized View

# @dp.table(name="src_sales_stream")
# def src_sales_stream():
#     df = spark.readStream.table("dbacademy.labuser14586003_1778253791.sales")
#     df = df.withColumn("date", to_date(col("date"), "MM-dd-yyyy"))
#     return df

# # Materialized View
# @dp.table(name="enr_sales_stream")
# def enr_sales_stream():
#     df = spark.readStream.table("src_sales_stream")
#     df = df.withColumn("revenue", col("revenue") * 1.05)
#     return df

# @dp.table(name="cur_sales_stream")
# def cur_sales_stream():
#     df = spark.readStream.table("enr_sales_stream")
#     df = df.groupBy("date").agg(sum("revenue").alias("total_revenue"))
#     return df
