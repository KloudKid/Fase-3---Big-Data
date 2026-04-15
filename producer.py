# Simulación de datos en tiempo real
# Importamos librerías necesarias
import time
import json
from kafka import KafkaProducer
import csv

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
# Abrimos el archivo CSV que contiene los datos
with open('siembra_palmira.csv', encoding='utf-8', errors='ignore') as file:
    reader = csv.DictReader(file)
# Recorrer cada fila del archivo
    for row in reader:
        # Enviamos cada fila al topic de Kafka
        producer.send('Siembras_Palmira', row)
        # Mostramos en consola lo que se está enviando
        print("Enviado:", row)
        # Esperamos 1 segundo antes de enviar el siguiente dato
        time.sleep(1)
