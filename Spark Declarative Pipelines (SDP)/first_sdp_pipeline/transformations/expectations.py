# from pyspark import pipelines as dp
# from pyspark.sql.functions import *

# rules = {
#     "rule1":"product_id IS NOT NULL",
#     "rule2":"updated_at IS NOT NULL",
# }

# @dp.table(name="product_table")
# @dp.expect_all_or_drop(rules)
# def product_table():
#     return spark.readStream.table("products")