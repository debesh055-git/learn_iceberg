echo "===== ICEBERG POC HEALTH CHECK =====" && \
echo "Date: $(date)" && \
echo "" && \
echo "JAVA VERSION" && \
java -version 2>&1 | head -1 && \
echo "" && \
echo "JAVA_HOME" && \
echo $JAVA_HOME && \
echo "" && \
echo "PYTHON VERSION" && \
python --version && \
echo "" && \
echo "PYSPARK VERSION" && \
python -c "import pyspark; print(pyspark.__version__)" && \
echo "" && \
echo "ICEBERG JAR" && \
find ~/.ivy2 -name "*iceberg-spark-runtime*jar" && \
echo "" && \
echo "WAREHOUSE DIRECTORY" && \
ls -ld warehouse && \
echo "" && \
echo "ICEBERG TABLES" && \
find warehouse -name "*.metadata.json"