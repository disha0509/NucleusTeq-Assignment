import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"
os.environ["HADOOP_HOME"] = r"C:\hadoop"
os.environ["PATH"] += os.pathsep + r"C:\hadoop\bin"

from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder.appName("TitanicDataProcessing").getOrCreate()

# Read from local CSV
df = spark.read.option("header", "true").csv("titanic.csv")

# Write in different formats
df.write.mode("overwrite").parquet("output/titanic_parquet")
df.write.mode("overwrite").json("output/titanic_json")

# Avro (requires spark-avro package)
# spark-submit --packages org.apache.spark:spark-avro_2.12:3.5.0 ...
#df.write.format("avro").mode("overwrite").save("output/titanic_avro")
