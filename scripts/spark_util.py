import os

# Reduce hostname warnings
os.environ["SPARK_LOCAL_IP"] = "127.0.0.1"

from pyspark.sql import SparkSession


def get_spark():

    spark = (
        SparkSession.builder
        .master("local[*]")
        .appName("IcebergDemo")

        # Disable Spark UI
        .config("spark.ui.enabled", "false")

        # Disable console progress bars
        .config("spark.ui.showConsoleProgress", "false")

        # Iceberg Runtime
        .config(
            "spark.jars.packages",
            "org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.5.2"
        )

        # Iceberg Extensions
        .config(
            "spark.sql.extensions",
            "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions"
        )

        # Catalog Configuration
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

    # Suppress Spark logs
    spark.sparkContext.setLogLevel("ERROR")

    return spark