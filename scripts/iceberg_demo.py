from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .master("local[*]")
    .appName("IcebergDemo")
    .config(
        "spark.jars.packages",
        "org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.5.2"
    )
    .config(
        "spark.sql.extensions",
        "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions"
    )
    .config(
        "spark.sql.catalog.demo",
        "org.apache.iceberg.spark.SparkCatalog"
    )
    .config(
        "spark.sql.catalog.demo.type",
        "hadoop"
    )
    .config(
        "spark.sql.catalog.demo.warehouse",
        "warehouse"
    )
    .getOrCreate()
)

df= spark.read.csv(
    "data/emp.csv",
    header=True,
    inferSchema=True
)

df.show()

df.writeTo(
   "demo.db.employee"
).append()

spark.read.table(
    "demo.db.employee"
).show()

spark.stop()