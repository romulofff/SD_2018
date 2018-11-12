import socket
import random
import time

server = input('Servidor: ')
port = input('Porta: ')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server,int(port)))
print('Lâmpada do quarto conectada ao servidor!')
on = True
def lampStatus(on):
    if(on):
        estado = "ligada"
    else:
        estado = "desligada"
    return estado

name = "Lâmpada do quartoEND"
s.send(name.encode('utf-8'))

while True:
    msg = "Estado atual: " + lampStatus(on)
    s.send(msg.encode('utf-8'))
    print('\n'+msg)
    toggle=input("\nDeseja pressionar o interruptor? ")
    if(toggle == 'sim'):
        on = not on 
    
s.close()   
    

