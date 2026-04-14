# Tarea 3 - Procesamientos de Datos con Apache Spark
# Autor: Juan Camilo López Melo
# Curso: Big Data
# Universidad Nacional Abierta y a Distancia – UNAD
# Año: 2026

* Descripción del proyecto

Este proyecto implementa una solución de procesamiento de datos utilizando tecnologías de Big Data, específicamente Apache Spark y Apache Kafka, aplicadas a un conjunto de datos abierto sobre tipos de siembra en el municipio de Palmira (Colombia).

El sistema permite realizar:

Procesamiento Batch para análisis histórico de datos.
Procesamiento en tiempo real (Streaming) simulando flujo de datos mediante Kafka.

* Dataset utilizado
Fuente: Datos Abiertos de Colombia
Nombre: Tipos de siembra en Palmira
Formato: CSV
URL: https://www.datos.gov.co/resource/dwff-8dr8.csv

El dataset contiene información sobre:

Año 2020-2021
Departamento
Municipio
Especie plantada
Cantidad de árboles

* Tecnologías utilizadas
Apache Spark (PySpark)
Apache Kafka
Python 3
Ubuntu (VirtualBox)
PuTTY (conexión remota)

* Estructura del proyecto
─ batch_siembras.py       # Procesamiento batch
─ kafka_producer.py       # Simulación de envío de datos (Producer)
─ streaming.py            # Procesamiento en tiempo real (Consumer con Spark)
─ siembra_palmira.csv     # Dataset
─ README.md               # Documentación del proyecto

* Instrucciones de ejecución
  
1. Descargar el dataset
wget "https://www.datos.gov.co/resource/dwff-8dr8.csv" -O siembra_palmira.csv

2. Ejecutar el procesamiento Batch
spark-submit batch_siembras.py
Este proceso realiza:
Limpieza de datos
Análisis por municipio
Suma de árboles por especie
Estadísticas generales

3. Iniciar servicios de Kafka
Iniciar Zookeeper
/opt/Kafka/bin/zookeeper-server-start.sh /opt/Kafka/config/zookeeper.properties
Iniciar Kafka
/opt/Kafka/bin/kafka-server-start.sh /opt/Kafka/config/server.properties

4. Crear el topic
/opt/Kafka/bin/kafka-topics.sh --create \
--bootstrap-server localhost:9092 \
--replication-factor 1 \
--partitions 1 \
--topic Siembras_Palmira

5. Ejecutar el productor
python3 kafka_producer.py

6. Ejecutar el consumidor (Streaming)
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3 streaming.py

Este script simula el envío de datos en tiempo real hacia Kafka.
