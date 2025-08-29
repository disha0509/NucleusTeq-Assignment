from pyspark.sql import SparkSession
import sys
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"


def main():
    if len(sys.argv) != 2:
        print("Usage: python remove_duplicates.py <csv_file>")
        sys.exit(-1)

    csv_file = sys.argv[1]

    # Create Spark session
    spark = SparkSession.builder \
        .appName("RemoveDuplicates") \
        .master("local[*]") \
        .getOrCreate()

    # Load dataset
    df = spark.read.csv(csv_file, header=True, inferSchema=True)

    print("📌 Original Data (with duplicates):")
    df.show()

    # Remove duplicates
    df_no_dup = df.dropDuplicates()

    print("\n📌 Data after removing duplicates:")
    df_no_dup.show()

    spark.stop()

if __name__ == "__main__":
    main()
