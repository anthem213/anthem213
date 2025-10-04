from pyspark.sql import *
from pyspark.sql.types import  *
from pyspark.sql.functions import *

spark = SparkSession.builder.master("local[4]").appName("demo").getOrCreate()



df = spark.createDataFrame("")

df.withColumn('rank',rank().over( Window.orderBy(col('salary').desc()))).filter(col('rank') == 1).drop(col('rank'))

spark.stop()


df.withColumn('rank', rank().over(Window.orderBy(col('salary').desc()))).filter(col('rank')==1).drop(col('rank'))