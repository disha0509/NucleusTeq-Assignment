import sys
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
import pyspark.sql.functions as F
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"


def main(input_file):
    spark = SparkSession.builder.appName("MovingAverage").getOrCreate()

    # Load CSV
    df = spark.read.csv(input_file, header=True, inferSchema=True)

    print("Input Data:")
    df.show()

    # Define window spec (ordered by date, looking at current row + 2 previous rows)
    window_spec = Window.orderBy("date").rowsBetween(-2, 0)

    # Calculate moving average of sales
    df_with_ma = df.withColumn("moving_avg", F.avg("sales").over(window_spec))

    print("Data with Moving Average (3-day window):")
    df_with_ma.show()

    spark.stop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python moving_average.py <input_csv>")
        sys.exit(-1)
    main(sys.argv[1])
