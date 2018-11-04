import time
import paho.mqtt.client as paho

def on_message(client, userdata, msg):
    if msg.payload.decode() == "Abrir":
        l1_status = True
        client.publish("/Portao", l1_status)#publish
    elif msg.payload.decode() == "Fechar":
        l1_status = False
        client.publish("/Portao", l1_status)#publish

broker="mosquitto.org"
broker="localhost"

l1_status = False

client= paho.Client("front_gate")
client.on_message = on_message
print("Conectando ao broker ",broker)
client.connect(broker)#connect
client.loop_start() #start loop to process received messages

# Inscrevendo no Controlador
print("Inscrevendo no Controlador")
client.subscribe("/Controlador/Portao")#subscribe
time.sleep(2)

print("Enviando status da lâmpada.")
try:
    while (True):
        client.publish("/Portao", l1_status)#publish
        time.sleep(60*1) #Espera 1 minuto
        
except KeyboardInterrupt:
    print("\nDesconectado.")
client.disconnect() #disconnect
client.loop_stop() #stop loop
