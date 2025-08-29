from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, countDistinct
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"


# Step 1: Initialize Spark session
spark = SparkSession.builder \
    .appName("E-Commerce Sales Analysis") \
    .master("local[*]") \
    .getOrCreate()

# Step 2: Load datasets
orders = spark.read.option("header", True).option("inferSchema", True) \
    .csv("case-study1/data/orders.csv")

users = spark.read.option("header", True).option("inferSchema", True) \
    .csv("case-study1/data/users.csv")

# Step 3: Total sales per product & top 10 products
orders = orders.withColumn("revenue", col("quantity") * col("price"))
sales_per_product = orders.groupBy("product_id") \
    .agg(_sum("revenue").alias("total_revenue")) \
    .orderBy(col("total_revenue").desc())

top10_products = sales_per_product.limit(10)

# Step 4: Top 5 locations by revenue
orders_with_users = orders.join(users, "user_id")
top5_locations = orders_with_users.groupBy("location") \
    .agg(_sum("revenue").alias("location_revenue")) \
    .orderBy(col("location_revenue").desc()) \
    .limit(5)

# Step 5: Repeat customers (>5 orders)
repeat_customers = orders.groupBy("user_id") \
    .agg(countDistinct("order_id").alias("total_orders")) \
    .filter(col("total_orders") > 5) \
    .join(users, "user_id")

# Step 6: Save results as Parquet
top10_products.write.mode("overwrite").parquet("case-study1/output/top10Products")
top5_locations.write.mode("overwrite").parquet("case-study1/output/top5Locations")
repeat_customers.write.mode("overwrite").parquet("case-study1/output/repeatCustomers")

print(" Analysis complete. Results saved in 'case study 1/output/'")

spark.stop()
