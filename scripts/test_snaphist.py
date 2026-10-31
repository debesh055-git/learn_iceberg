from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .master("local[*]")
    .appName("IcebergSnapshotDemo")
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

print("===== SNAPSHOTS =====")

spark.sql("""
SELECT *
FROM demo.db.employee.snapshots
""").show(truncate=False)

print("===== DATA FILES =====")

spark.sql("""
SELECT *
FROM demo.db.employee.files
""").show(truncate=False)

spark.stop()