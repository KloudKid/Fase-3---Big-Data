# Simulación de datos en tiempo real

import time
import json
from kafka import KafkaProducer
import csv

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

with open('siembra_palmira.csv', encoding='utf-8', errors='ignore') as file:
    reader = csv.DictReader(file)

    for row in reader:
        producer.send('Siembras_Palmira', row)
        print("Enviado:", row)
        time.sleep(1)
