from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, IntegerType

spark = SparkSession.builder.appName("StreamingSiembrasPalmira").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

# Leer desde Kafka
df = (spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "Siembras_Palmira")
    .load())

# Convertir a string
data = df.selectExpr("CAST(value AS STRING)")

# 🔹 Definir esquema (ajustable)
schema = StructType() \
    .add("vigencia", StringType()) \
    .add("departamento", StringType()) \
    .add("municipio", StringType()) \
    .add("especie_plantada", StringType()) \
    .add("cantidad_arboles", StringType())

# 🔹 Convertir JSON a columnas
parsed = data.select(from_json(col("value"), schema).alias("data")).select("data.*")

# 🔹 Mostrar datos organizados
query = (parsed.writeStream
    .outputMode("append")
    .format("console")
    .start())

query.awaitTermination()
