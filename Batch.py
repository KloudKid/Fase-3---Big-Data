from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Crear sesión de Spark
spark = SparkSession.builder.appName("BatchSiembrasPalmira").getOrCreate()

# Cargar el archivo CSV
df = spark.read.csv("siembra_palmira.csv", header=True, inferSchema=True)

# Mostrar estructura del dataset
df.printSchema()

# Mostrar primeras filas
df.show(5)

# Limpieza de datos (eliminar nulos)
df = df.dropna()

# Análisis 1: cantidad de registros por municipio
df.groupBy("municipio").count().show()

# Análisis 2: total de árboles por especie
df.groupBy("especie_plantada").sum("cantidad_arboles").show()

# Análisis 3: registros por departamento
df.groupBy("departamento").count().show()

# Análisis 4: promedio de árboles
df.select(avg("cantidad_arboles")).show()

# Estadísticas generales
df.describe().show()

# Finalizar sesión
spark.stop()
