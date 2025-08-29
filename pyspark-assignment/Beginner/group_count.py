from pyspark.sql import SparkSession
import sys
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"


def main():
    if len(sys.argv) != 3:
        print("Usage: python group_count.py <csv_file> <group_column>")
        sys.exit(-1)

    csv_file = sys.argv[1]
    group_column = sys.argv[2]

    # Create Spark session
    spark = SparkSession.builder \
        .appName("GroupByCount") \
        .master("local[*]") \
        .getOrCreate()

    # Load dataset
    df = spark.read.csv(csv_file, header=True, inferSchema=True)

    print(" Input Data:")
    df.show()

    # Group by column and count
    grouped = df.groupBy(group_column).count()

    print(f"\n Row count per group by '{group_column}':")
    grouped.show()

    spark.stop()

if __name__ == "__main__":
    main()
