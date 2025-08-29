from pyspark import SparkConf, SparkContext
import sys
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"


def main():
    if len(sys.argv) != 2:
        print("Usage: python charcount.py <input_file>")
        sys.exit(-1)

    input_file = sys.argv[1]

    conf = SparkConf().setAppName("CharacterCount").setMaster("local[*]")
    # disable Hadoop auth issue on Windows
    conf.set("spark.hadoop.hadoop.security.authentication", "simple")
    sc = SparkContext(conf=conf)

    # Read file
    lines = sc.textFile(input_file)

    # Split lines into characters
    chars = lines.flatMap(lambda line: list(line))

    # Map each character to (char, 1)
    char_pairs = chars.map(lambda ch: (ch, 1))

    # Reduce by key to count occurrences
    char_counts = char_pairs.reduceByKey(lambda a, b: a + b)

    # Collect and print results
    for ch, count in char_counts.collect():
        if ch == " ":
            print(f"'(space)' : {count}")
        elif ch == "\t":
            print(f"'(tab)' : {count}")
        elif ch == "\n":
            print(f"'(newline)' : {count}")
        else:
            print(f"'{ch}' : {count}")

    sc.stop()

if __name__ == "__main__":
    main()
