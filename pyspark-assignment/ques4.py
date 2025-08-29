from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"
os.environ["HADOOP_HOME"] = r"C:\hadoop"
os.environ["PATH"] += os.pathsep + r"C:\hadoop\bin"

# Initialize SparkSession
spark = SparkSession.builder.appName("EmployeeSalaryUpdate").getOrCreate()

data = [
    (1, "John", 50000, "HR"),
    (2, "Alice", 60000, "IT"),
    (3, "Bob", 70000, "HR")
]

df = spark.createDataFrame(data, ["empid", "empname", "salary", "department"])

# Decrease salary of HR by 10%
df_updated = df.withColumn(
    "salary",
    when(col("department") == "HR", col("salary") * 0.9).otherwise(col("salary"))
)

# Write to HDFS (adjust path to your HDFS config)
df_updated.write.mode("overwrite").parquet("employees_updated.parquet")
df_check = spark.read.parquet("employees_updated.parquet")
df_check.show()
