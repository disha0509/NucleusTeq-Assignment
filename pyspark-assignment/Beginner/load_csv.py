from pyspark.sql import SparkSession
import sys
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"


def main():
    if len(sys.argv) != 2:
        print("Usage: python load_csv.py <csv_file>")
        sys.exit(-1)

    csv_file = sys.argv[1]

    # Create Spark session
    spark = SparkSession.builder \
        .appName("CSVLoader") \
        .master("local[*]") \
        .getOrCreate()

    # Load CSV file with header
    df = spark.read.csv(csv_file, header=True, inferSchema=True)

    # Print schema
    print("📌 Schema of CSV file:")
    df.printSchema()

    # Show sample data
    print("📌 Sample data:")
    df.show()

    spark.stop()

if __name__ == "__main__":
    main()
