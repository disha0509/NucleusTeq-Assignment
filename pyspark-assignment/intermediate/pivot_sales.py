import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"


def main(input_file):
    spark = SparkSession.builder.appName("PivotExample").getOrCreate()

    # Read CSV
    df = spark.read.csv(input_file, header=True, inferSchema=True)

    print(" Input Data:")
    df.show()

    # Pivot on region and aggregate sales by product
    pivot_df = df.groupBy("product").pivot("region").agg(sum("sales"))

    print(" Pivoted Data (Total Sales by Region):")
    pivot_df.show()

    spark.stop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pivot_sales.py <input_csv>")
        sys.exit(-1)
    main(sys.argv[1])
