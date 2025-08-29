from pyspark.sql import SparkSession
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["PYSPARK_PYTHON"] = os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/disha/OneDrive/Documents/pyspark-practice/venv310/Scripts/python.exe"

def main():
    # Update path to your JDBC driver
    spark = SparkSession.builder \
    .appName("SparkJDBCExample") \
    .config("spark.jars", "C:/Program Files/PostgreSQL/17") \
    .getOrCreate()


    # JDBC connection properties
    jdbc_url = "jdbc:postgresql://localhost:5432/db"  # change db
    jdbc_properties = {
        "user": "myuser",
        "password": "Password",
        "driver": "org.postgresql.Driver"
    }

    # ------------------ READ ------------------
    print("Reading data from database...")
    df = spark.read.jdbc(url=jdbc_url, table="public.employees", properties=jdbc_properties)
    df.show()

    # ------------------ TRANSFORM ------------------
    # Example: Filter employees with salary > 50000
    df_filtered = df.filter(df["salary"] > 50000)

    # ------------------ WRITE ------------------
    print("Writing filtered data to another table...")
    df_filtered.write.jdbc(
        url=jdbc_url,
        table="public.high_salary_employees",  # new table
        mode="overwrite",  # overwrite / append
        properties=jdbc_properties
    )

    spark.stop()

if __name__ == "__main__":
    main()
