import socket
import random


server = input('Servidor: ')
port = input('Porta: ')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server,int(port)))
print('Portão conectado ao servidor!')

on = True

def gateStatus(on):
    if(on):
        estado = "aberto"
    else:
        estado = "fechado"
    return estado

name = "PortãoEND"
s.send(name.encode('utf-8'))

while True:
    msg = "Estado atual: " + gateStatus(on)
    s.send(msg.encode('utf-8'))
    if gateStatus(on) == "aberto":
        print("\nPortão Aberto!")
        toggle=input("\nFechar o portão? ")
    else:
        print("\nPortão Fechado!")
        toggle=input("\nAbrir o portão? ")
        
    if(toggle == 'sim'):
        on = not on 

s.close()   
    

