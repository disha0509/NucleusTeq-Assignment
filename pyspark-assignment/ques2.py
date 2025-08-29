from pyspark.sql.functions import unix_timestamp, col, round
from pyspark.sql import SparkSession

import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"

# Initialize SparkSession
spark = SparkSession.builder.appName("ProcessDuration").getOrCreate()

# Sample data
data = [
    (1, "Process A", "2023-01-01 08:00:00", "2023-01-01 10:30:00"),
    (2, "Process B", "2023-01-01 09:00:00", "2023-01-01 15:00:00"),
    (3, "Process C", "2023-01-01 11:00:00", "2023-01-01 13:00:00")
]

df = spark.createDataFrame(data, ["process_id", "process_name", "strt_dt_time", "end_dt_time"])

# Convert to timestamp and calculate duration in hours
df_duration = df.withColumn("start_ts", unix_timestamp("strt_dt_time")) \
                .withColumn("end_ts", unix_timestamp("end_dt_time")) \
                .withColumn("duration_hrs", round((col("end_ts") - col("start_ts")) / 3600, 2))

# Get max duration row
max_duration = df_duration.orderBy(col("duration_hrs").desc()).limit(1)
max_duration.show()
