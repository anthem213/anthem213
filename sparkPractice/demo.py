from pyspark.sql.functions import udf
from pyspark.sql import *
from pyspark.sql.types import  *
from pyspark.sql.functions import *


def count_words(a):
    l=[]
    d = dict()
    for i in a.split(" "):
        i = i.lower()
        if i not in l:
            l.append(i)
            d[i] = 1
        else:
            d[i] = d.get(i)+1
    return d

my_udf = udf(count_words)

schema = "id Integer, name String, age Integer, region String"

data  = [(1,'Anthem is busy ',23, 'SA'), (1,'Anthem is not busy',23, 'RB'), (2,'ASD is there',23, 'SA'), (6,'RRR is a good film',33, 'SA')]

spark = SparkSession.builder.master("local[4]").appName("demo").getOrCreate()

df = spark.createDataFrame(data,schema)


df1  = df.select(trim('name').alias('name')).withColumn('count_words', my_udf(col('name')))

df1.show(truncate=False)






