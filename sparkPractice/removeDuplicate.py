from pyspark.sql import *
from pyspark.sql.types import  *
from pyspark.sql.functions import *

spark = SparkSession.builder.master("local[4]").appName("demo").getOrCreate()

schema = "id Integer, name String, age Integer, region String"

data  = [(1,'Anthem',23, 'SA'), (1,'Anthem',23, 'RB'), (2,'ASD',23, 'SA'), (6,'RRRR',33, 'SA')]

df = spark.createDataFrame(data,schema)

df.show()

#id, name, age, region

df1 = df.dropDuplicates(subset=["name", "age"]).orderBy(col('id').desc())
df1.show()


df.withColumn('rn', row_number().over(Window.partitionBy('name','age').orderBy(col('id'))))\
    .filter(col('rn')==1).orderBy('id').show()

