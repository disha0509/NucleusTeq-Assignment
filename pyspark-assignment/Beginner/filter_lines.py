from pyspark import SparkConf, SparkContext
import sys
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"


def main():
    if len(sys.argv) != 3:
        print("Usage: python filter_lines.py <input_file> <keyword>")
        sys.exit(-1)

    input_file = sys.argv[1]
    keyword = sys.argv[2]

    conf = SparkConf().setAppName("FilterLines").setMaster("local[*]")
    sc = SparkContext(conf=conf)

    # Read input file
    lines = sc.textFile(input_file)

    # Filter lines containing the keyword
    filtered_lines = lines.filter(lambda line: keyword in line)

    # Collect and print
    for line in filtered_lines.collect():
        print(line)

    sc.stop()

if __name__ == "__main__":
    main()
