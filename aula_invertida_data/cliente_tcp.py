'''
############ SISTEMAS DISTRIBUÍDOS ############
Aula Invertida - Representação de Dados
GRUPO: Rômulo Férrer Filho, Rhaniel Magalhães, Marcus Vinicius, Pablo Grisi 
'''

import socket
import json

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 6665            # Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

dest = (HOST, PORT)

tcp.connect(dest)

while True:
    tcp.send("Get 10 movies from IMDB".encode())
    data = tcp.recv(4096)
    if not data: break
    filmes = json.loads(data)
    for i in range(len(filmes)):
        print(filmes[i]['titulo'] + " foi lançado em: " + str(filmes[i]['ano']))
    break

tcp.close()