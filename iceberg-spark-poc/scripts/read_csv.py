from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Demo")
    .getOrCreate()
)

df = spark.read.csv(
    "data/emp.csv",
    header=True,
    inferSchema=True
)

df.show()