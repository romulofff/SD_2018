import time
import paho.mqtt.client as paho
import random
import decimal

broker="mosquitto.org"
broker="localhost"

client= paho.Client("termometer-002")

print("Conectando ao broker ",broker)
client.connect(broker)#connect
client.loop_start() #start loop to process received messages
print("Enviando temperatura a cada 5 segundos.")

try:
    while (True):
        temp = random.uniform(22.0, 25.0)
        temp = decimal.Decimal(temp).quantize(decimal.Decimal('.01'))
        client.publish("/Temperatura/Quarto",str(temp)+'°C')#publish
        time.sleep(2.5)
except KeyboardInterrupt:
    print("\nDesconectado.")

client.disconnect() #disconnect
client.loop_stop() #stop loop
