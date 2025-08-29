from pyspark.sql import SparkSession
from pyspark.sql.functions import col, rand, floor, concat, lit
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"

def main():
    spark = SparkSession.builder.appName("SaltingExample").getOrCreate()

    # Sample skewed dataset
    data = [("A", 1), ("A", 2), ("A", 3), ("A", 4), ("B", 5), ("C", 6)]
    df_skewed = spark.createDataFrame(data, ["key", "value"])

    print("Original Skewed Data:")
    df_skewed.show()

    # Add salt column (random int between 0 and 2)
    df_skewed_salted = df_skewed.withColumn("salt", (floor(rand() * 3)).cast("int"))

    # Create salted key by concatenating key + "_" + salt
    df_skewed_salted = df_skewed_salted.withColumn(
        "salted_key", concat(col("key"), lit("_"), col("salt").cast("string"))
    )

    print("After Adding Salt:")
    df_skewed_salted.show()

    # Simulate another dataset to join with
    data_lookup = [("A_0", "Alpha"), ("A_1", "Alpha"), ("A_2", "Alpha"),
                   ("B_0", "Beta"), ("B_1", "Beta"), ("B_2", "Beta"),
                   ("C_0", "Gamma"), ("C_1", "Gamma"), ("C_2", "Gamma")]

    df_lookup = spark.createDataFrame(data_lookup, ["salted_key", "desc"])

    print("Lookup Data with Salted Keys:")
    df_lookup.show()

    # Perform join on salted key
    df_joined = df_skewed_salted.join(df_lookup, "salted_key", "inner")

    print("Joined Data After Salting:")
    df_joined.show()

    spark.stop()

if __name__ == "__main__":
    main()
