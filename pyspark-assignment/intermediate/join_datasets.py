import sys
from pyspark.sql import SparkSession
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"


def main(customers_file, orders_file):
    spark = SparkSession.builder.appName("JoinExample").getOrCreate()

    # Load datasets
    customers = spark.read.csv(customers_file, header=True, inferSchema=True)
    orders = spark.read.csv(orders_file, header=True, inferSchema=True)

    print("Customers:")
    customers.show()

    print("Orders:")
    orders.show()

    # Inner Join
    inner_join = customers.join(orders, on="customer_id", how="inner")
    print("Inner Join Result:")
    inner_join.show()

    # Left Join
    left_join = customers.join(orders, on="customer_id", how="left")
    print("Left Join Result:")
    left_join.show()

    # Right Join
    right_join = customers.join(orders, on="customer_id", how="right")
    print("Right Join Result:")
    right_join.show()

    spark.stop()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python join_datasets.py <customers_csv> <orders_csv>")
        sys.exit(-1)
    main(sys.argv[1], sys.argv[2])
