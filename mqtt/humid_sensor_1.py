import time
import paho.mqtt.client as paho
import random
import decimal

broker="mosquitto.org"
broker="localhost"

client= paho.Client("humidity-001")

print("Conectando ao broker ",broker)
client.connect(broker)#connect
client.loop_start() #start loop to process received messages
print("Enviando umidade a cada 5 segundos.")

try:
    while (True):
        humid = random.uniform(22.0, 25.0)
        humid = decimal.Decimal(humid).quantize(decimal.Decimal('.01'))
        client.publish("/Umidade/Sala",str(humid)+'%')#publish
        time.sleep(2.5)
except KeyboardInterrupt:
    print("\nDesconectado.")

client.disconnect() #disconnect
client.loop_stop() #stop loop
