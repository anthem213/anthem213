# Input data as a list of tuples
from pyspark.sql import SparkSession
from pyspark.sql.functions import collect_list

spark = SparkSession.builder.master("local[4]").appName("demo").getOrCreate()

data = [
    ("a", "aa", 1),
    ("a", "aa", 2),
    ("b", "bb", 5),
    ("b", "bb", 3),
    ("b", "bb", 4)
]

# Create a DataFrame with the input data
df = spark.createDataFrame(data, ["Col 1", "Col 2", "Col 3"])

df.groupBy("Col 1" , "Col 2").agg(collect_list('Col 3').alias('Col 3')).show()