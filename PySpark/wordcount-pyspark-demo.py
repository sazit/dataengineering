# first need to install pyspark -> pip install pyspark, or python -m pip install pyspark
from pyspark import SparkContext

# Initialize Spark Context
sc = SparkContext("local", "Word Count Example")

# Read text file
text_file = sc.textFile("data/data.txt")

# Perform word count, map;reduce
counts = (
    text_file.flatMap(lambda line: line.split(" "))
    .map(lambda word: (word, 1))
    .reduceByKey(lambda a, b: a + b)
)

# Sort, then output the counts
sorted_counts = counts.sortBy(lambda x: x[1], ascending=False)
for (word, count) in sorted_counts.collect():
    print(word ,":" ,count)

# Stop Spark Context
sc.stop()

