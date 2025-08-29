from pyspark.sql import SparkSession
import sys
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"


def main():
    if len(sys.argv) != 2:
        print("Usage: python total_sales_per_product.py <csv_file>")
        sys.exit(-1)

    csv_file = sys.argv[1]

    # Create Spark session
    spark = SparkSession.builder \
        .appName("TotalSalesPerProduct") \
        .master("local[*]") \
        .getOrCreate()

    # Load CSV file
    df = spark.read.option("header", "true").option("inferSchema", "true").csv(csv_file)

    print(" Input Sales Data:")
    df.show()

    # Calculate total sales per product (quantity * price)
    sales_df = df.withColumn("total", df["quantity"] * df["price"])

    # Group by product and sum total sales
    result_df = sales_df.groupBy("product").sum("total").withColumnRenamed("sum(total)", "total_sales")

    print("\n Total Sales per Product:")
    result_df.show()

    spark.stop()

if __name__ == "__main__":
    main()
