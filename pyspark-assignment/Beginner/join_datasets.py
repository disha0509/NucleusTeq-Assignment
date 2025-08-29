from pyspark.sql import SparkSession
import sys
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"


def main():
    if len(sys.argv) != 3:
        print("Usage: python join_datasets.py <employees_csv> <departments_csv>")
        sys.exit(-1)

    emp_file = sys.argv[1]
    dept_file = sys.argv[2]

    # Create Spark session
    spark = SparkSession.builder \
        .appName("JoinDatasets") \
        .master("local[*]") \
        .getOrCreate()

    # Load datasets
    employees = spark.read.csv(emp_file, header=True, inferSchema=True)
    departments = spark.read.csv(dept_file, header=True, inferSchema=True)

    print(" Employees Schema:")
    employees.printSchema()
    print(" Departments Schema:")
    departments.printSchema()

    # Perform inner join on dept_id
    joined = employees.join(departments, employees.dept_id == departments.dept_id, "inner") \
                    .select("emp_id", "name", employees.dept_id, "dept_name")

    print("\n Joined Data:")
    joined.show()

    spark.stop()

if __name__ == "__main__":
    main()
