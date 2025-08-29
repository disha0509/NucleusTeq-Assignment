import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import Row
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"

spark = SparkSession.builder \
    .appName("Practice") \
    .master("local[*]") \
    .config("spark.ui.enabled", "true") \
    .config("spark.driver.extraJavaOptions", "--enable-native-access=ALL-UNNAMED") \
    .config("spark.executor.extraJavaOptions", "--enable-native-access=ALL-UNNAMED") \
    .getOrCreate()

print("Spark UI:", spark.sparkContext.uiWebUrl)

list = ["apple", "banana", "cherry", "mango", "orange"]
rdd = spark.sparkContext.parallelize(list)
print(list)
print(rdd.collect())

mapped_rdd = rdd.map(lambda x: Row(value=x))
df = spark.createDataFrame(mapped_rdd)
df.show()


input("Press Enter to stop...")