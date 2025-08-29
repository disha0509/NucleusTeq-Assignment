import sys
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import col, sum as _sum
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"


def main(input_file):
    spark = SparkSession.builder.appName("RunningTotalSales").getOrCreate()

    # Load CSV
    df = spark.read.csv(input_file, header=True, inferSchema=True)

    print(" Input Data:")
    df.show()

    # Define window (partition by product, ordered by date)
    window_spec = Window.partitionBy("product").orderBy("date") \
                        .rowsBetween(Window.unboundedPreceding, Window.currentRow)

    # Running total calculation
    df_running = df.withColumn("running_total", _sum("sales").over(window_spec))

    print(" Running Total of Sales:")
    df_running.show()

    spark.stop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python running_total_sales.py <input_file>")
        sys.exit(-1)
    main(sys.argv[1])
