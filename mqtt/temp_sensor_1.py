import time
import paho.mqtt.client as paho

broker="mosquitto.org"
broker="localhost"
broker="192.168.25.7"
client= paho.Client("termometer-001")

print("Conectando ao broker ",broker)
client.connect(broker, 1883)#connect
client.loop_start() #start loop to process received messages
print("Enviando temperatura a cada 5 segundos.")

try:
    while (True):
        # client.publish("/Temperatura/Sala","22°C")#publish
        client.publish("/romulo","MEU PAU TA DURO")#publish
        time.sleep(2.5)
except KeyboardInterrupt:
    print("\nDesconectado.")

client.disconnect() #disconnect
client.loop_stop() #stop loop
