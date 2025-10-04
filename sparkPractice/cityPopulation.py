from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import col

# Initialize Spark Session (as per your provided setup)
spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()


def etl(city_data):
    # Filter for Japan's country code ("JPN")
    japan_cities_df = city_data.filter(col("COUNTRYCODE") == "JPN")

    # Aggregate (sum) the POPULATION column.
    # We use F.sum because functions are imported as F.
    total_population_df = japan_cities_df \
        .agg(F.sum("POPULATION").alias("Total Population"))

    return total_population_df


# --- Data Setup and Execution ---

# 1. Define Input Data (Required for a runnable script)
schema = "Id INT, Name STRING, COUNTRYCODE STRING, DISTRICT STRING, POPULATION BIGINT"
data = [
    # JPN Cities
    (1, "Tokyo", "JPN", "Kanto", 13929286),
    (2, "Osaka", "JPN", "Kansai", 2691167),
    (3, "Kyoto", "JPN", "Kansai", 1474570),
    (4, "Nagoya", "JPN", "Chubu", 2304879),
    (5, "Fukuoka", "JPN", "Kyushu", 1587352),
    (6, "Hiroshima", "JPN", "Chugoku", 1192011),
    # Non-JPN Cities (for testing filter)
    (7, "Seoul", "KOR", "Seoul", 9962351),
    (8, "Shanghai", "CHN", "Shanghai", 27058480),
]

# Create the DataFrame named city_data
city_data = spark.createDataFrame(data, schema)

# 2. Run the ETL function
result_df = etl(city_data)

# 3. Display the result
print("--- Total Population of Japan ---")
result_df.show(truncate=False)

# Optional: Stop the Spark session if running outside a Databricks environment
spark.stop()
