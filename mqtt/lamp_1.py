import time
import paho.mqtt.client as paho

def on_message(client, userdata, msg):
    if msg.payload.decode() == "Ligar":
        l1_status = True
        client.publish("/Lampadas/L1", l1_status)#publish
    elif msg.payload.decode() == "Desligar":
        l1_status = False
        client.publish("/Lampadas/L1", l1_status)#publish

broker="mosquitto.org"
broker="localhost"

l1_status = False

client= paho.Client("lamp-001")
client.on_message = on_message
print("Conectando ao broker ",broker)
client.connect(broker)#connect
client.loop_start() #start loop to process received messages

# Inscrevendo no Controlador
print("Inscrevendo no Controlador")
client.subscribe("/Controlador/Lampadas/L1")#subscribe
time.sleep(2)

print("Enviando status da lâmpada.")
try:
    while (True):
        client.publish("/Lampadas/L1", l1_status)#publish
        time.sleep(60*1) #Espera 1 minuto
        
except KeyboardInterrupt:
    print("\nDesconectado.")
client.disconnect() #disconnect
client.loop_stop() #stop loop
