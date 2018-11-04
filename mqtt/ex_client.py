import time
import paho.mqtt.client as paho
broker="mosquitto.org"
broker="localhost"
#define callback
def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))

client= paho.Client("client-001") 
client.on_message=on_message
#####
print("connecting to broker ",broker)
client.connect(broker)#connect
client.loop_start() #start loop to process received messages
print("subscribing ")
client.subscribe("/teste")#subscribe
time.sleep(2)
print("publishing ")
i = 0
while (i<10):
    client.publish("/teste","123")#publish
    time.sleep(1)
    i+=1
client.disconnect() #disconnect
client.loop_stop() #stop loop
