import sys
from pyspark.sql import SparkSession
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"


def main(input_file, output_dir):
    spark = SparkSession.builder.appName("CSVtoParquet").getOrCreate()

    # Read CSV
    df = spark.read.csv(input_file, header=True, inferSchema=True)

    print(" Input CSV Data:")
    df.show()

    # Write as Parquet
    df.write.mode("overwrite").parquet(output_dir)

    print(f" CSV converted to Parquet and saved at: {output_dir}")

    spark.stop()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python csv_to_parquet.py <input_csv> <output_parquet_dir>")
        sys.exit(-1)
    main(sys.argv[1], sys.argv[2])
