from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, trim

spark = SparkSession.builder.master("local[4]").appName("demo").getOrCreate()

data = [
    ("Alice", "Badminton, Tennis"),
    ("Greg", "Cricket, Baseball"),
    ("Julie", "Swimming, Basket ball"),
    ("Alan", "Tennis, Swimming"),
    ("Xian", "Badminton, Baseball")
]

# Create a DataFrame with the input data
df = spark.createDataFrame(data, ["Name", "Sport"])

df1 = df.withColumn('Sport', explode((split('Sport', ','))))

#df1.withColumn('Sport', trim('Sport')).show()
df1.select('Name', trim('Sport')).show()