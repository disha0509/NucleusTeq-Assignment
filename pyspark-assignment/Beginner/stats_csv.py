from pyspark.sql import SparkSession
import sys
from pyspark.sql.functions import avg, min, max
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"


def main():
    if len(sys.argv) != 3:
        print("Usage: python stats_csv.py <csv_file> <numeric_column>")
        sys.exit(-1)

    csv_file = sys.argv[1]
    column = sys.argv[2]

    # Create Spark session
    spark = SparkSession.builder \
        .appName("CSVStatistics") \
        .master("local[*]") \
        .getOrCreate()

    # Load CSV
    df = spark.read.csv(csv_file, header=True, inferSchema=True)

    # Print schema
    print("📌 Schema of the CSV:")
    df.printSchema()

    # Compute statistics
    stats = df.select(
        avg(column).alias("Average"),
        min(column).alias("Minimum"),
        max(column).alias("Maximum")
    )

    print(f"\n📊 Statistics for column '{column}':")
    stats.show()

    spark.stop()

if __name__ == "__main__":
    main()
