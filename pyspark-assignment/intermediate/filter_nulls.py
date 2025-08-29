import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim

import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"

def main(input_file):
    spark = SparkSession.builder.appName("FilterNulls").getOrCreate()

    # Read CSV
    df = spark.read.csv(input_file, header=True, inferSchema=True)

    print(" Input Data:")
    df.show()

    # Filter out rows where 'name' or 'age' is null or empty
    df_clean = df.filter(
        (col("name").isNotNull()) & (trim(col("name")) != "") &
        (col("age").isNotNull()) & (trim(col("age").cast("string")) != "")
    )

    print(" Cleaned Data (no null/empty values):")
    df_clean.show()

    spark.stop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python filter_nulls.py <input_csv>")
        sys.exit(-1)
    main(sys.argv[1])
