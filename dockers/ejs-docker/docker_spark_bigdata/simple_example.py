from pyspark.sql import SparkSession

# Iniciar una sesión de Spark
spark = SparkSession.builder.master("spark://spark-master:7077").appName("SimpleApp").getOrCreate()

# Crear un simple RDD
data = [1, 2, 3, 4, 5]
distData = spark.sparkContext.parallelize(data)

# Realizar una operación simple
print("Suma de los elementos:", distData.reduce(lambda a, b: a + b))

# Finalizar la sesión de Spark
spark.stop()
