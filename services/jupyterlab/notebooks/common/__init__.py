import os
import pyspark
from pyspark.sql import SparkSession

NESSIE_URI = "http://nessie:19120/api/v1"
AWS_ACCESS_KEY = "minio"
AWS_SECRET_KEY = "minio123"
AWS_S3_ENDPOINT = "http://minio:9000"
WAREHOUSE = "s3a://lake/"


def getOrCreateSparkSession() -> pyspark.sql.SparkSession:
    """Get or create a Spark session."""
    conf = (
        pyspark.SparkConf()
            .setAppName('app_name')
            .set("spark.sql.execution.pyarrow.enabled", "true")
            .set(
                "spark.jars.packages",
                f"org.apache.iceberg:iceberg-spark-runtime-3.2_2.12:1.4.2,org.projectnessie.nessie-integrations:nessie-spark-extensions-3.2_2.12:0.74.0",
            )
            .set('spark.sql.catalog.nessie', 'org.apache.iceberg.spark.SparkCatalog')
            .set('spark.sql.catalog.nessie.uri', NESSIE_URI)
            .set('spark.sql.catalog.nessie.ref', 'main')
            .set('spark.sql.catalog.nessie.authentication.type', 'NONE')
            .set('spark.sql.catalog.nessie.catalog-impl', 'org.apache.iceberg.nessie.NessieCatalog')
            .set("spark.sql.catalog.nessie.warehouse", "file://" + os.getcwd() + "/spark-warehouse/iceberg")
            .set('spark.hadoop.fs.s3a.access.key', 'minio')
            .set('spark.hadoop.fs.s3a.secret.key', 'minio123')
            .set('spark.hadoop.fs.s3a.endpoint', "http://minio:9000")
            .set('spark.hadoop.fs.s3a.connection.ssl.enabled', "false")
            .set('spark.hadoop.fs.s3a.path.style.access', "true")
            .set(
                "spark.sql.extensions",
                "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions,org.projectnessie.spark.extensions.NessieSparkSessionExtensions",
            )
    )
    
    return SparkSession.builder.config(conf=conf).getOrCreate()
    