import time
import paho.mqtt.client as paho

def on_message(client, userdata, msg):
    if msg.payload.decode('utf-8') == "Abrir":
        global gate_status
        gate_status = True
        client.publish("/Portao", gate_status)#publish
        time.sleep(3)
    elif msg.payload.decode('utf-8') == "Fechar":
        gate_status = False
        client.publish("/Portao", gate_status)#publish
        time.sleep(3)

broker="mosquitto.org"
broker="localhost"

gate_status = False

client= paho.Client("front_gate")
client.on_message = on_message
print("Conectando ao broker ",broker)
client.connect(broker)#connect
client.loop_start() #start loop to process received messages

# Inscrevendo no Controlador
print("Inscrevendo no Controlador")
client.subscribe("/Controlador/Portao")#subscribe
time.sleep(2)

print("Enviando status do Portão.")
try:
    while (True):
        if gate_status == True:
            g_status = "Aberto"
        elif gate_status == False:
            g_status = "Fechado"
        client.publish("/Portao", g_status)#publish
        time.sleep(60*1) #Espera 1 minuto
        
except KeyboardInterrupt:
    print("\nDesconectado.")
client.disconnect() #disconnect
client.loop_stop() #stop loop
