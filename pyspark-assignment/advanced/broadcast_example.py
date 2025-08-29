import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"


def main(input_file):
    spark = SparkSession.builder.appName("BroadcastExample").getOrCreate()

    # Load CSV
    df = spark.read.csv(input_file, header=True, inferSchema=True)

    print(" Original Sales Data:")
    df.show()

    # Small lookup table (product → category)
    product_category = {
        "Laptop": "Electronics",
        "Mouse": "Accessories",
        "Keyboard": "Accessories",
        "Monitor": "Electronics"
    }

    # Broadcast the dictionary
    bc_lookup = spark.sparkContext.broadcast(product_category)

    # Use the broadcast variable in a UDF
    def map_category(product):
        return bc_lookup.value.get(product, "Unknown")

    

    category_udf = udf(map_category, StringType())

    # Add a new column "category" using broadcasted lookup
    df_with_category = df.withColumn("category", category_udf(df["product"]))

    print(" Sales Data with Categories (using Broadcast):")
    df_with_category.show()

    spark.stop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python broadcast_example.py <input_csv>")
        sys.exit(-1)
    main(sys.argv[1])
