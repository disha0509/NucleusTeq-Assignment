# case-study2/streaming_logs.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, window, sum as _sum
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"

def main():
    spark = SparkSession.builder \
        .appName("Streaming Log Analytics") \
        .getOrCreate()
    spark.sparkContext.setLogLevel("WARN")

    # Schema for incoming logs
    schema = StructType([
        StructField("user_id", StringType(), True),
        StructField("video_id", StringType(), True),
        StructField("watch_time", IntegerType(), True),
        StructField("timestamp", TimestampType(), True)
    ])

    # Read streaming input from CSV files (dropped in input folder)
    df = spark.readStream \
        .schema(schema) \
        .option("sep", ",") \
        .csv("case-study2/input/")

    # ------------------------
    # Aggregations with watermark
    # ------------------------

    # User watch time (5 min window, filter >= 2 minutes)
    user_watch_time = df \
        .withWatermark("timestamp", "10 minutes") \
        .groupBy(
            window(col("timestamp"), "5 minutes"),
            col("user_id")
        ).agg(
            _sum("watch_time").alias("total_watch_time")
        ).filter(col("total_watch_time") >= 120)

    # Top videos (10 min window)
    top_videos = df \
        .withWatermark("timestamp", "15 minutes") \
        .groupBy(
            window(col("timestamp"), "10 minutes"),
            col("video_id")
        ).agg(
            _sum("watch_time").alias("total_watch_time")
        ).orderBy(col("total_watch_time").desc())

    # ------------------------
    # Outputs
    # ------------------------

    # Write user watch time → Parquet
    query_parquet = user_watch_time.writeStream \
        .outputMode("append") \
        .format("parquet") \
        .option("path", "case-study2/output/") \
        .option("checkpointLocation", "case-study2/checkpoints/user_watch_time/") \
        .start()

    # Write top 5 videos → Console
    query_console = top_videos.writeStream \
        .outputMode("complete") \
        .format("console") \
        .option("truncate", "false") \
        .start()

    query_parquet.awaitTermination()
    query_console.awaitTermination()

if __name__ == "__main__":
    main()
