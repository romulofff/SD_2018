import time
import paho.mqtt.client as paho
import random
import decimal

broker="mosquitto.org"
broker='172.20.10.3'
port=1883

client= paho.Client("humidity-001")

print("Conectando ao broker ",broker)
client.connect(broker, port)#connect
client.loop_start() #start loop to process received messages
print("Enviando umidade a cada 5 segundos.")

try:
    while (True):
        humid = random.uniform(64.0, 79.0)
        humid = decimal.Decimal(humid).quantize(decimal.Decimal('.01'))
        client.publish("/Umidade/Sala",str(humid)+'%')#publish
        print(str(humid)+'%')
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\nDesconectado.")

client.disconnect() #disconnect
client.loop_stop() #stop loop
