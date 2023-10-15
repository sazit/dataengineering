import org.apache.spark
@main def simpleScals() =
    val conf = new SparkConf().setAppName("SparkMR").setMaster("local[*")
    val sc = new SparkContext(conf)

    val lines = sc.textFile ("data/sampledata.txt")

    val words = lines.flatMap(l => l.split(" "))
    val pairs = splitLines.map (w => (w,1))

    val wordCount = pairs.reduceByKey((a,b) => a+b)

    wordCount.collect.forEach(println)