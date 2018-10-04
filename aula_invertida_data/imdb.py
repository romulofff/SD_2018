'''
############ SISTEMAS DISTRIBUÍDOS ############
Aula Invertida - Representação de Dados
GRUPO: Rômulo Férrer Filho, Rhaniel Magalhães, Marcus Vinicius, Pablo Grisi 
'''

import json
import sys, errno

# Atividade para sala
# Questão 1: Representando os filmes em formato JSON
IMDB = [
    {
        "FilmeID": 0,
        "titulo": "Vingadores: Infinity War",
        "ano": 2018,
        "Avaliacao_IMDB": 8.6,
        "Filmes": ["Thor: Ragnarok", "Capitão América: Guerra Civil", "Doutor Estranho"],
        "url": "https://www.youtube.com/watch?v=t_ULBP6V9bg"
    },
    {
        "FilmeID": 1,
        "titulo": "Batman: Dark Knight",
        "ano": 2008,
        "Avaliacao_IMDB": 9.0,
        "Filmes": ["Batman: Begins", "Batman: Dark Knight Rises", "Inception"],
        "url": "https://www.youtube.com/watch?v=EXeTwQWrcwY"
    },
    {
        "FilmeID": 2,
        "titulo": "Lord of the Rings: The Return of the King",
        "ano": 2003,
        "Avaliacao_IMDB": 8.9,
        "Filmes": ["Lord of the Rings: The Fellowship of the Ring", "Lord of the Rings: The Two Towers", "Forrest Gump"],
        "url": "https://www.youtube.com/watch?v=r5X-hFf6Bwo"
    },
    {
        "FilmeID": 3,
        "titulo": "Pulp Fiction",
        "ano": 1994,
        "Avaliacao_IMDB": 8.9,
        "Filmes": ["Fight Club", "The Silence of the Lambs", "Inception"],
        "url": "https://www.youtube.com/watch?v=s7EdQ4FqbhY"
    },
    {
        "FilmeID": 4,
        "titulo": "Fight Club",
        "ano": 1999,
        "Avaliacao_IMDB": 8.8,
        "Filmes": ["Seven", "Matrix", "Forrest Gump"],
        "url": "https://www.youtube.com/watch?v=BdJKm16Co6M"
    },
    {
        "FilmeID": 5,
        "titulo": "Predator",
        "ano": 1987,
        "Avaliacao_IMDB": 7.8,
        "Filmes": ["Alien", "Terminator", "Aliens"],
        "url": "https://www.youtube.com/watch?v=Y1txEAywdiw"
    },
    {
        "FilmeID": 6,
        "titulo": "The Matrix",
        "ano": 1999,
        "Avaliacao_IMDB": 8.7,
        "Filmes": ["Fight Club", "Forrest Gump", "Inception"],
        "url": "https://www.youtube.com/watch?v=2KnZac176Hs"
    },
    {
        "FilmeID": 7,
        "titulo": "Alien",
        "ano": 1979,
        "Avaliacao_IMDB": 8.5,
        "Filmes": ["Aliens", "The Shining", "Terminator"],
        "url": "https://www.youtube.com/watch?v=LjLamj-b0I8"
    },
    {
        "FilmeID": 8,
        "titulo": "Terminator",
        "ano": 1984,
        "Avaliacao_IMDB": 8.0,
        "Filmes": ["Alien", "Back to the Future", "Jurassic Park"],
        "url": "https://www.youtube.com/watch?v=k64P4l2Wmeg"
    },
    {
        "FilmeID": 9,
        "titulo": "Jurassic Park",
        "ano": 1993,
        "Avaliacao_IMDB": 8.1,
        "Filmes": ["Indiana Jones: Raiders of the Lost Ark", "Lost World: Jurassic Park", "Jurassic World"],
        "url": "https://www.youtube.com/watch?v=lc0UehYemQA"
    }
]

filmes = json.dumps(IMDB)
# print(filmes)

# Questão 2:
import socket

HOST, PORT = '127.0.0.1', 6665
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(1)

enc_filmes = filmes.encode()
while True:
    con, cliente = tcp.accept()
    print("Conectado por ", cliente)
    while True:
        msg = con.recv(1024).decode()
        print("Mensagem recebida", msg)
        try:
            con.sendall(enc_filmes)
        except IOError as e:
            if e.errno == errno.EPIPE:
                pass
        break    
    print("Finalizando conexão do cliente ", cliente)
    con.close()