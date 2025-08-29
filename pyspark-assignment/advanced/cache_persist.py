import sys
import time
from pyspark.sql import SparkSession
from pyspark.storagelevel import StorageLevel
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"

def main(input_file):
    spark = SparkSession.builder.appName("CachePersistExample").getOrCreate()

    # Load CSV
    df = spark.read.csv(input_file, header=True, inferSchema=True)

    print("Original Data:")
    df.show()

    # Without cache/persist
    print("\n Running actions WITHOUT cache/persist:")
    start = time.time()
    print("Total amount:", df.groupBy().sum("amount").collect())
    print("Max amount:", df.agg({"amount": "max"}).collect())
    end = time.time()
    print("Execution time (no cache):", end - start, "seconds")

    # With cache
    print("\n⚡ Running actions WITH cache():")
    df_cached = df.cache()  # stored in memory
    df_cached.count()  # materialize cache

    start = time.time()
    print("Total amount:", df_cached.groupBy().sum("amount").collect())
    print("Max amount:", df_cached.agg({"amount": "max"}).collect())
    end = time.time()
    print("Execution time (with cache):", end - start, "seconds")

    # With persist (MEMORY_AND_DISK)
    print("\n Running actions WITH persist(MEMORY_AND_DISK):")
    df_persisted = df.persist(StorageLevel.MEMORY_AND_DISK)
    df_persisted.count()  # materialize persist

    start = time.time()
    print("Total amount:", df_persisted.groupBy().sum("amount").collect())
    print("Max amount:", df_persisted.agg({"amount": "max"}).collect())
    end = time.time()
    print("Execution time (with persist):", end - start, "seconds")

    spark.stop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python cache_persist.py <input_csv>")
        sys.exit(-1)
    main(sys.argv[1])
