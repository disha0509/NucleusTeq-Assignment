import sys
from pyspark.sql import SparkSession
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"

def main(input_file):
    spark = SparkSession.builder.appName("AccumulatorExample").getOrCreate()
    sc = spark.sparkContext

    # Load CSV
    df = spark.read.csv(input_file, header=True, inferSchema=True)

    print("Original Transactions:")
    df.show()

    # Create accumulator on driver
    high_value_acc = sc.accumulator(0)

    # Broadcast accumulator into the function via closure
    def check_transaction(row):
        if row.amount > 500:
            high_value_acc.add(1)   # use .add(), not +=
        return row

    # Trigger action
    df.rdd.foreach(check_transaction)   # use foreach instead of collect()

    # Print result (after action)
    print(f" Number of high-value transactions (> 500): {high_value_acc.value}")

    spark.stop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python accumulator_example.py <input_csv>")
        sys.exit(-1)
    main(sys.argv[1])
