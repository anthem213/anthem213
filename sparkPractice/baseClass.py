from pyspark.sql import SparkSession


class BaseClass:
    def __init__(self,app_name = "DefaultSparkApp", master_url = 'local[4]'):
        self.app_name = app_name
        self.master_url = master_url
        self.spark = None
        self._initialize_spark()

    def _initialize_spark(self):
        """
        Creates or retrieves the singleton SparkSession.
        """
        print(f"--- Initializing Spark Session: {self.app_name} ---")
        try:
            self.spark = SparkSession.builder \
                .master(self.master_url) \
                .appName(self.app_name) \
                .getOrCreate()
            print("Spark Session created successfully.")
        except Exception as e:
            print(f"Error initializing Spark Session: {e}")
            raise

    def stop_spark(self):
        """
        Stops the active SparkSession.
        """
        if self.spark:
            self.spark.stop()
            print(f"--- Spark Session '{self.app_name}' stopped. ---")