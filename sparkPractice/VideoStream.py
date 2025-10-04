import datetime

from pyspark.sql import SparkSession, DataFrame

from pyspark.sql.functions import *

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(video_stream_df: DataFrame):
    current_year = datetime.datetime.now().year
    df = video_stream_df.groupBy('video_id', 'title', 'duration', 'release_year')\
        .agg(sum(col('view_count')).alias('view_count'))\
        .filter((col('view_count') > 1000000) & (col('release_year') >= current_year-6))\
        .orderBy(col('duration'))

    return df


schema = "video_id INT, title STRING, genre STRING, release_year INT, duration BIGINT, view_count INT"
data = [
    (1, "Amazing Adventure", "Action", 2020, 120, 2500000),
    (2, "Sci-fi World", "Sci-fi", 2018, 140, 800000),
    (3, "Mysterious Island", "Drama", 2022, 115, 1500000),
    (4, "Uncharted Realms", "Action", 2019, 134, 3200000),
    (5, "Journey to the Stars", "Sci-fi", 2021, 128, 1100000)
]


df1 = spark.createDataFrame(data, schema =schema)

result_df = etl(df1)

result_df.show()