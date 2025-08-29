from pyspark import SparkConf, SparkContext
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"


def main():
    conf = SparkConf().setAppName("WordCount").setMaster("local[*]")
    sc = SparkContext(conf=conf)

    
    lines = sc.textFile("Beginner/input.txt")

    
    words = lines.flatMap(lambda line: line.split())

    
    word_pairs = words.map(lambda word: (word, 1))

    
    word_counts = word_pairs.reduceByKey(lambda a, b: a + b)

    
    for word, count in word_counts.collect():
        print(f"{word} : {count}")

    sc.stop()

if __name__ == "__main__":
    main()
