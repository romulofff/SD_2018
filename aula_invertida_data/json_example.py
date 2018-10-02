'''
############ SISTEMAS DISTRIBUÍDOS ############
Aula Invertida - Representação de Dados
GRUPO: Rômulo Férrer Filho, Rhaniel Magalhães, Marcus Vinicius, Pablo Grisi 
'''
# Inicialmente importamos o pacote 'json' do Python
import json

# Agora devemos criar objetos que serão transformados em JSON
contacts = [
    {
        "nome": "Romulo",
        "cidade": "Fortaleza",
        "idade": 20
    },
    {
        "nome": "Pablo",
        "cidade": "Rio de Janeiro",
        "idade": 20
    },
    {
        "nome": "Rhaniel",
        "cidade": "Itapipoca",
        "idade": 21
    },
    {
        "nome": "Marcus",
        "cidade": "Fortaleza",
        "idade": 21
    }
] # fim contacts

# Convertendo para JSON
toJSON = json.dumps(contacts)
print(toJSON)

# Lendo JSON
fromJSON = json.loads(toJSON)

print(fromJSON[3]["idade"])