import sys
from pyspark.sql import SparkSession
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"


def main(input_file, col1, col2):
    spark = SparkSession.builder.appName("CorrelationExample").getOrCreate()

    # Load CSV
    df = spark.read.csv(input_file, header=True, inferSchema=True)

    print(" Input Data:")
    df.show()

    # Calculate correlation
    corr_value = df.stat.corr(col1, col2)

    print(f" Correlation between '{col1}' and '{col2}': {corr_value}")

    spark.stop()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python correlation.py <input_csv> <col1> <col2>")
        sys.exit(-1)
    main(sys.argv[1], sys.argv[2], sys.argv[3])
