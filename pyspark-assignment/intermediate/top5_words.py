from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col, lower, count
import sys
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"


def main():
    if len(sys.argv) != 2:
        print("Usage: python top5_words.py <text_file>")
        sys.exit(-1)

    text_file = sys.argv[1]

    # Create Spark session
    spark = SparkSession.builder \
        .appName("Top5Words") \
        .master("local[*]") \
        .getOrCreate()

    lines = spark.read.text(text_file)

    
    words = lines.select(explode(split(lower(col("value")), "\\s+")).alias("word"))

    
    words = words.filter(words.word != "")

    
    word_counts = words.groupBy("word").agg(count("*").alias("count"))

    
    top5 = word_counts.orderBy(col("count").desc()).limit(5)

    print("📌 Top 5 Most Frequent Words:")
    top5.show()

    spark.stop()

if __name__ == "__main__":
    main()
