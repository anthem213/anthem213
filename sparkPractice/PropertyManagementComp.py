from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import *

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(prop_landlords: DataFrame, prop_properties: DataFrame):
	# Write code here
	prop_landlords.dropDuplicates(subset=['landlord_id'])
	prop_properties.dropDuplicates(subset=['property_id'])
	df = prop_properties.join(prop_landlords, on  = 'landlord_id', how= 'inner')
	df_result = df.groupBy('landlord_id','first_name','last_name').agg(sum(col('rent'))\
		.alias('total_rent')).select('landlord_id', concat_ws(' ', 'first_name', 'last_name').alias('landlord_name'),'total_rent')

	return df_result

property_tuples = [
    (1, 101, "Apartment", 1500, 1000, "Seattle"),
    (2, 101, "Condo", 1200, 800, "Seattle"),
    (3, 102, "House", 2000, 1500, "Bellevue"),
    (4, 103, "Apartment", 1800, 1200, "Redmond"),
    (5, 103, "Condo", 1000, 700, "Redmond")
]
property_schema = "property_id INT, landlord_id INT, property_type STRING, rent INT, square_feet INT, city STRING"

landlord_tuples = [
    (101, "John", "Smith", "john.smith@example.com", "555-123-4567"),
    (102, "Jane", "Doe", "jane.doe@example.com", "555-234-5678"),
    (103, "Bob", "Johnson", "bob.johnson@example.com", "555-345-6789"),
    (104, "Mary", "Williams", "mary.williams@example.com", "555-456-7890")
]

landlord_schema = "landlord_id INT, first_name STRING, last_name STRING, email STRING, phone STRING"

df1 = spark.createDataFrame(property_tuples, schema=property_schema)
df2 = spark.createDataFrame(landlord_tuples, schema=landlord_schema)

df1.show()
df2.show()

df_final  = etl(df2,df1)
df_final.show()

