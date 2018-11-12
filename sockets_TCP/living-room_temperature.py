import socket
import random
import time

server = input('Servidor: ')
port = input('Porta: ')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server,int(port)))
print('Sensor de temperatura da sala conectado ao servidor!')

def my_temperature():
    temp = random.uniform(19.0, 24.0)
    return round(temp, 2)

name = "Sensor de temperatura SEND"
s.send(name.encode('utf-8'))

while True:    
    msg = "Temperatura atual da sala: " + str(my_temperature())
    s.send(msg.encode('utf-8'))
    time.sleep(5)

s.close()   
    

