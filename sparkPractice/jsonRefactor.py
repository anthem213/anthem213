from pyspark.sql import *
from pyspark.sql.types import  *
from pyspark.sql.functions import *

spark = SparkSession.builder.master("local[4]").appName("demo").getOrCreate()

data = [
  {
    "product_id": 902,
    "inventory_id": [
      10301,
      10302
    ]
  },
  {
    "product_id": 901,
    "inventory_id": [
      10301,
      10302,
      10303
    ]
  }
]

schema = "product_id Integer,inventory_id Array<INT> "
df = spark.createDataFrame(data, schema)


#method 1
df.withColumn('inventory_id', explode(col('inventory_id'))).orderBy(col('product_id')).show()

#or

#method 2
df.selectExpr('product_id', 'explode(inventory_id) as inventory_id').orderBy(col('product_id')).show()

