from pyspark.sql import SparkSession
import sys
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"


def main():
    if len(sys.argv) != 2:
        print("Usage: python load_json_extract.py <json_file>")
        sys.exit(-1)

    json_file = sys.argv[1]

    # Create Spark session
    spark = SparkSession.builder \
        .appName("LoadJSONExtract") \
        .master("local[*]") \
        .getOrCreate()

    # Load JSON file
    df = spark.read.json(json_file)

    print("📌 Full DataFrame:")
    df.show()

    # Extract only specific fields (name, dept, salary)
    selected_df = df.select("name", "dept", "salary")

    print("\n📌 Extracted Fields:")
    selected_df.show()

    spark.stop()

if __name__ == "__main__":
    main()
