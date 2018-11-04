import time
import paho.mqtt.client as paho

broker="mosquitto.org"
broker="localhost"

client= paho.Client("controller")

print("Conectando ao broker ",broker)
client.connect(broker)#connect
client.loop_start() #start loop to process received messages
print("Enviando temperatura a cada 5 segundos.")

try:
    while (True):
        client.publish("/Controlador/Lampadas/L1", "Desligar")#publish
        time.sleep(2.5)
except KeyboardInterrupt:
    print("\nDesconectado.")

client.disconnect() #disconnect
client.loop_stop() #stop loop
