import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, lower, col
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"


def main(input_file):
    spark = SparkSession.builder.appName("TokenizeAndCountWords").getOrCreate()

    # Load text file
    df = spark.read.text(input_file)
    print("Input Sentences:")
    df.show(truncate=False)

    # Tokenize: split sentences into words
    words_df = (
        df.select(explode(split(lower(col("value")), "\\W+")).alias("word"))
        .filter(col("word") != "")   # remove empty tokens
    )

    print("Tokenized Words:")
    words_df.show()

    # Count unique words
    word_count = words_df.groupBy("word").count().orderBy(col("count").desc())

    print("Unique Word Counts:")
    word_count.show()

    spark.stop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tokenize_count.py <input_text_file>")
        sys.exit(-1)
    main(sys.argv[1])
