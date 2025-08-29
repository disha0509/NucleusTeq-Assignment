import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import expr
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"


def main(input_file):
    spark = SparkSession.builder.appName("UnpivotExample").getOrCreate()

    # Read CSV
    df = spark.read.csv(input_file, header=True, inferSchema=True)

    print(" Input Wide Data:")
    df.show()

    
    unpivot_expr = "stack(3, 'East', East, 'West', West, 'North', North) as (region, sales)"
    df_unpivoted = df.select("product", expr(unpivot_expr))

    print(" Unpivoted Data (Long Format):")
    df_unpivoted.show()

    spark.stop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python unpivot_sales.py <input_csv>")
        sys.exit(-1)
    main(sys.argv[1])
