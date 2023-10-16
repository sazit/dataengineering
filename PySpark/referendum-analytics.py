from pyspark.sql import SparkSession
import pandas as pd

# Initialize Spark Session
spark = SparkSession.builder.master("local[1]").appName('Referendum-Analytics').getOrCreate()

# Read CSV with PySpark
nsw_polling_csv = "referendum-data/by-polling-place/ReferendumPollingPlaceResultsByStateDownload-29581-NSW.csv"
df = spark.read.option("header", "false").csv(nsw_polling_csv)

# Set second line as header
header = [row.asDict() for row in df.head(1)][0]
df = df.toDF(*header.values())

# Skip the header line to keep the rest as data
df = df.filter(df[list(header.values())[0]] != list(header.values())[0])

# Convert to Pandas DataFrame
pdf = df.toPandas()

print(pdf)
