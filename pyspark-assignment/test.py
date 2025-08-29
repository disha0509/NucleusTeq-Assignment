from pyspark.sql import SparkSession
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"
spark = SparkSession.builder \
    .appName("PySpark Fix Test") \
    .master("local[*]") \
    .getOrCreate()
data = [("Shantanu", 29), ("Alice", 33)]
df = spark.createDataFrame(data, ["Name", "Age"])
df.show()
spark.stop()