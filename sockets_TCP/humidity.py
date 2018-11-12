import socket
import random
import time

server = input('Servidor: ')
port = input('Porta: ')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server,int(port)))
print('Sensor de umidade conectado ao servidor!')

global humidity

def my_humidity():
    humidity = random.uniform(0, 100)
    return round(humidity, 2)

name = "Sensor de umidadeEND"
s.send(name.encode('utf-8'))

while True:
    humidity=my_humidity()
    msg = "Umidade atual: " + str(humidity)
    s.send(msg.encode('utf-8'))
    time.sleep(5)

s.close()   
