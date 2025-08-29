import sys
from pyspark.sql import SparkSession
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"

def main(input_file):
    spark = SparkSession.builder.appName("FilterMultipleConditions").getOrCreate()

    # Load CSV
    df = spark.read.csv(input_file, header=True, inferSchema=True)

    print("📌 Original Data:")
    df.show()

    # -------------------------
    # Filtering conditions:
    # 1. Salary > 5000
    # 2. Age < 40
    # 3. Department = "IT"
    # -------------------------
    filtered_df = df.filter(
        (df.salary > 5000) & (df.age < 40) & (df.department == "IT")
    )

    print("✅ Filtered Data (salary > 5000, age < 40, department = IT):")
    filtered_df.show()

    spark.stop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python filter_conditions.py <input_csv>")
        sys.exit(-1)
    main(sys.argv[1])
