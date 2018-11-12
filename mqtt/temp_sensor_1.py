import time
import paho.mqtt.client as paho
import random
import decimal

broker="mosquitto.org"
broker='172.20.10.3'
port=1883

client= paho.Client("termometer-001")

print("Conectando ao broker ",broker)
client.connect(broker, port)#connect
client.loop_start() #start loop to process received messages
print("Enviando temperatura a cada 5 segundos.")

random.seed()
try:
    while (True):
        temp = random.uniform(19.0, 24.0)
        temp = decimal.Decimal(temp).quantize(decimal.Decimal('.01'))
        client.publish("/Temperatura/Sala",str(temp)+'°C')#publish
        print(str(temp)+'°C')
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\nDesconectado.")

client.disconnect() #disconnect
client.loop_stop() #stop loop
