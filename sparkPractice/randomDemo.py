from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.master("local[4]").appName("demo").getOrCreate()

schema = "Name String, Age Integer"
data = [("Anthem", 11), ("Anthem", 20), ("Demigod", 10), ("Raven", 66)]
#df = spark.read.load("path", format = 'csv', headers = True, sep=',', schema=schema)

df = spark.createDataFrame(data, schema)
df.show(2)

#df.createOrReplaceTempView('table_1')

df2 = df.filter(col('Age') > 20)
df1 = df.select("Name").distinct().count()
# print(df.distinct().count())
# print(df1)

#df.union(df2).show()


#df.filter((col('Name').startswith('A') ) & (col('Age') > 20)).show()


#df.groupBy('Name').agg(sum('Age')).show()

df.select("Name",df.Age + 100).show()



df.select(expr("Name as first_name"), expr("Age + 10 as New_age")).show()

b =df.agg(avg('Age')).collect()[0][0]
print(b)