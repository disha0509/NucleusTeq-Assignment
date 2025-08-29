from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col, lower, collect_list
import sys
import itertools
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"


def main():
    if len(sys.argv) != 2:
        print("Usage: python word_cooccurrence.py <text_file>")
        sys.exit(-1)

    text_file = sys.argv[1]

    spark = SparkSession.builder \
        .appName("WordCooccurrence") \
        .master("local[*]") \
        .getOrCreate()

    # Load text file into DataFrame
    lines = spark.read.text(text_file)

    # Split lines into words (lowercased)
    words_per_line = lines.select(
        split(lower(col("value")), "\\s+").alias("words")
    )

    # Generate all pairs of words from each line
    def generate_pairs(words):
        pairs = []
        unique_words = list(set(words))  # avoid duplicates from same line
        for combo in itertools.combinations(sorted(unique_words), 2):
            pairs.append(combo)
        return pairs

    # Register UDF-free transformation using flatMap
    rdd = words_per_line.rdd.flatMap(lambda row: generate_pairs(row["words"]))

    # Convert to DataFrame
    pairs_df = rdd.toDF(["word1", "word2"])

    # Count co-occurrence frequency
    cooccurrence = pairs_df.groupBy("word1", "word2").count().orderBy(col("count").desc())

    print("📌 Word Co-occurrence:")
    cooccurrence.show(truncate=False)

    spark.stop()

if __name__ == "__main__":
    main()
