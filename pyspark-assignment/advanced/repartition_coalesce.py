import sys
from pyspark.sql import SparkSession
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"

def main(input_file):
    spark = SparkSession.builder.appName("RepartitionCoalesceExample").getOrCreate()

    # Load CSV
    df = spark.read.csv(input_file, header=True, inferSchema=True)

    print(" Original Data:")
    df.show()

    # Show number of partitions in original DataFrame
    print("Original partitions:", df.rdd.getNumPartitions())

    # Repartition into 4 partitions
    df_repartitioned = df.repartition(4)
    print("After Repartition (4 partitions):", df_repartitioned.rdd.getNumPartitions())

    # Coalesce into 2 partitions
    df_coalesced = df_repartitioned.coalesce(2)
    print("After Coalesce (2 partitions):", df_coalesced.rdd.getNumPartitions())

    spark.stop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python repartition_coalesce.py <input_csv>")
        sys.exit(-1)
    main(sys.argv[1])
