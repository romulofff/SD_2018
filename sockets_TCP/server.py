import select
import socket
import sys
import re


host = input('Host: ') # Digitar o endereço para o servidor
port = input('Porta: ') # Digitar a porta para o servidor
max_conn = 5  # Números de conexões a serem aceitas
maxsize = 1024 # Tamanho máximo do buffer recebido, em bytes

#Inicializando o servidor e aceitando comunicações

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind((host,int(port))) 
server.listen(max_conn) 
input = [server,] #Lista com todas as conexões ativas 

socket_names = ['Servidor',] #Nomes das conexões para melhor identificação

#Loop infinito para receber novas conexões e mensagens
running = 1
while running: 
  inputready,outputready,exceptready = select.select(input,[],[]) 

  for s in inputready: #Olhar todos os sockets com dados disponíveis

    if s == server: #Quando o socket for o servidor, entra nesse loop
      
      client, address = server.accept()
      if client:
          new=True
      input.append(client) #Adiciona o novo cliente à lista de sockets


    else:
        
      if(new):   #Verifica se é um novo cliente e armazena seu nome na lista de conexões
          name=s.recv(maxsize).decode()
          m = re.search('(.+?)END', name)
          if m:
            name = m.group(1)
          socket_names.append(name)
          print(name + " conectado com sucesso!")
          print("\nSockets conectados")
          print(socket_names)
          new=False
          
      
      
      # Sockets com dados disponíveis
      data = s.recv(maxsize) 
      if data:
        print('%s >> %s'%(socket_names[input.index(s)], data))
        
      else: #Se recv() retornar NULL, encerra o socket
        
        s.close()
        socket_names.remove(socket_names[input.index(s)])
        input.remove(s) 

server.close()
