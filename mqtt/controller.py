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
    # while (True):
    client.publish("/Controlador/Lampadas/L1", "Ligar")#publish
    client.publish("/Controlador/Portao", "Abrir")#publish
    time.sleep(4)
except KeyboardInterrupt:
    print("\nDesconectado.")

client.disconnect() #disconnect
client.loop_stop() #stop loop
