from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import *
from pyspark.sql import Window as W
import pyspark
import datetime
import json

from pyspark.sql.functions import *

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(df: DataFrame):
	# Write code here
     df_result = df.select('user_id', split(col('email'),'@')[1].alias('email_domain'), regexp_replace(col("phone"), r"^\d{6}", "******"))
     return df_result



user_contact_schema = "user_id INT, email STRING, phone BIGINT"

data = [
    (1, "alice@example.com", 5551234567),
    (2, "bob@domain.net", 5559876543),
    (3, "carol@email.org", 5551239876),
    (4, "dave@site.com", 5554567890),
    (5, "eve@platform.io", 5559871234)
]

df1 = spark.createDataFrame(data, schema=user_contact_schema)
df_result = etl(df1)
df_result.show()