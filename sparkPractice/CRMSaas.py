import datetime

from pyspark.sql import SparkSession, DataFrame

from pyspark.sql.functions import *

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()


def etl(customers: DataFrame, orders: DataFrame, products:DataFrame):

    df = customers.join(orders, customers.customer_id == orders.customer_id, 'right')
    df1 = df.join(products, df.customer_id == products.product_id, 'inner' )
    df_final = df1.withColumn('customer_name', concat_ws(' ', col('first_name'), col('last_name')))\
    .select("category", "customer_name",  "email", "order_date", "order_id", "product_name")
    return df_final


# solution from app

def etl_2(customers, orders, products):
    # Join customers → orders → products
    joined_df = customers.join(
        orders, on="customer_id", how="inner"
    ).join(
        products, on="product_id", how="inner"
    )

    # Select and rename fields as per required output
    result_df = joined_df.select(
        "order_id",
        concat_ws(" ", "first_name", "last_name").alias("customer_name"),
        col("email").alias("customer_email"),
        col("product_name"),
        col("category").alias("product_category"),
        "order_date"
    )

    return result_df