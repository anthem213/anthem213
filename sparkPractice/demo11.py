import datetime

from pyspark.sql import SparkSession, DataFrame

from pyspark.sql.functions import *

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()
schema = "video_id INT, title STRING, genre STRING, release_year INT, duration BIGINT, view_count INT"
data = [
    (1, "Amazing Adventure", "Action", 2020, 120, 2500000),
    (2, "Sci-fi World", "Sci-fi", 2018, 140, 800000),
    (3, "Mysterious Island", "Drama", 2022, 115, 1500000),
    (4, "Uncharted Realms", "Action", 2019, 134, 3200000),
    (5, "Journey to the Stars", "Sci-fi", 2021, 128, 1100000)
]

print( datetime.datetime.now().year)
df = spark.createDataFrame(data, schema =schema)

df2 = df.withColumn('year_diff', datediff(year(current_date()), col('release_year').cast('date')))
df2.show()
