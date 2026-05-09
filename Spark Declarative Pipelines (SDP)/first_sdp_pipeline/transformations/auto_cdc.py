# from pyspark import pipelines as dp
# from pyspark.sql.functions import *


# dp.create_streaming_table("product_scd_type1")
# dp.create_streaming_table("product_scd_type2")

# @dp.temporary_view()
# def product_source():
#     df = spark.readStream.table("products")
#     return df

# dp.create_auto_cdc_flow(
#   target="product_scd_type2",  # The customer table being materialized
#   source="product_source",  # the incoming CDC
#   keys=["product_id"],  # what we'll be using to match the rows to upsert
#   sequence_by=col("updated_at"),  # de-duplicate by operation date, getting the most recent value
# #   apply_as_deletes=expr("operation = 'DELETE'"),  # DELETE condition
#   except_column_list=["updated_at"],
#   stored_as_scd_type="2"
# )


# dp.create_auto_cdc_flow(
#   target="product_scd_type1",  # The customer table being materialized
#   source="product_source",  # the incoming CDC
#   keys=["product_id"],  # what we'll be using to match the rows to upsert
#   sequence_by=col("updated_at"),  # de-duplicate by operation date, getting the most recent value
# #   apply_as_deletes=expr("operation = 'DELETE'"),  # DELETE condition
#   except_column_list=["updated_at"],
#   stored_as_scd_type="1"
# )
