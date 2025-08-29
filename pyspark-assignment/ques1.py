from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import col, lag, round
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"

spark = SparkSession.builder.appName("RevenueIncrease").getOrCreate()

# Sample data
data = [
    (1, 'A', 2020, 1000),
    (2, 'A', 2021, 1500),
    (3, 'A', 2022, 1800),
    (4, 'B', 2020, 2000),
    (5, 'B', 2021, 2200),
]

df = spark.createDataFrame(data, ["id", "org_id", "year", "revenue"])

# Window partition by org_id and order by year
window_spec = Window.partitionBy("org_id").orderBy("year")

# Calculate previous year's revenue
df_with_lag = df.withColumn("prev_revenue", lag("revenue").over(window_spec))

# Calculate percentage increase
result = df_with_lag.withColumn("pct_increase", 
                round(((col("revenue") - col("prev_revenue")) / col("prev_revenue")) * 100, 2))

result.show()
