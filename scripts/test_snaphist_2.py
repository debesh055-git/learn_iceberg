from spark_util import get_spark

spark = get_spark()

print("===== SNAPSHOTS =====")

spark.sql("""
SELECT
    file_path,
    record_count,
    file_size_in_bytes
FROM demo.db.employee.files
""").show(truncate=False)

print("===== DATA FILES =====")

spark.sql("""
SELECT
    snapshot_id,
    operation,
    committed_at
FROM demo.db.employee.snapshots
""").show(truncate=False)

spark.stop()