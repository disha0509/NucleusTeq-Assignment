import sys
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"


def main(input_csv, output_parquet):
    spark = SparkSession.builder.appName("SimpleETLPipeline").getOrCreate()

    # -----------------
    # Extract: Load CSV
    # -----------------
    df = spark.read.csv(input_csv, header=True, inferSchema=True)
    print("📌 Extracted Data:")
    df.show()

    
    transformed_df = (
        df.filter(df.salary > 5000)
          .withColumn("bonus", df.salary * 0.10)
        .withColumn("department", F.upper(df.department))
    )

    print("📌 Transformed Data:")
    transformed_df.show()

    # -----------------
    # Load: Write to Parquet
    # -----------------
    transformed_df.write.mode("overwrite").parquet(output_parquet)
    print(f"✅ Data written to Parquet at: {output_parquet}")

    spark.stop()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python etl_pipeline.py <input_csv> <output_parquet_dir>")
        sys.exit(-1)

    main(sys.argv[1], sys.argv[2])
