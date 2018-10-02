import socket
import json

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 6661            # Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

dest = (HOST, PORT)

tcp.connect(dest)

while True:
    tcp.send("Get 10 movies from IMDB".encode())
    data = tcp.recv(4096)
    if not data: break
    filmes = json.loads(data)
    print(filmes)
    break
tcp.close()