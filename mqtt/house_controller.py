import ssl
import sys

import paho.mqtt.client
import paho.mqtt.publish

from tkinter import *

def on_connect(client, userdata, flags, rc):
    print('connected (%s)' % client._client_id)
    client.subscribe(topic='/Temperatura/Sala')
    client.subscribe(topic='/Temperatura/Quarto')
    client.subscribe(topic='/Portao')
    client.subscribe(topic='/Umidade/Sala')
    client.subscribe(topic='/Lampadas/L1')

def on_message(mosq, obj, msg):
    print(msg.topic+" "+str(msg.payload.decode("utf-8")))

def on_message_temperatura_sala(client, userdata, message):
    global temperatura_message_sala_var
    temperatura_message_sala_var = str(message.payload.decode("utf-8"))

def on_message_temperatura_quarto(client, userdata, message):
    global temperatura_message_quarto_var
    temperatura_message_quarto_var = str(message.payload.decode("utf-8"))

def on_message_umidade(client, userdata, message):
    global umidade_message_var
    umidade_message_var = str(message.payload.decode("utf-8"))

def on_message_portao(client, userdata, message):
    global portao_message_var
    if str(message.payload.decode("utf-8")) == 'Aberto':
        portao_message_var = True
    elif str(message.payload.decode("utf-8")) == 'Fechado':
        portao_message_var = False

def on_button_portao():
    global portao_message_var
    global client

    if portao_message_var:
        client.publish("/Controlador/Portao", 'Fechar')
    elif not portao_message_var:
        client.publish("/Controlador/Portao", 'Abrir')

def on_message_lampada(client, userdata, message):
    global lampada_message_var
    if str(message.payload.decode("utf-8")) == 'Ligada':
        lampada_message_var = True
    elif str(message.payload.decode("utf-8")) == 'Desligada':
        lampada_message_var = False

def on_button_lampada():
    global lampada_message_var
    global client

    if lampada_message_var:
        client.publish("/Controlador/Lampadas/L1", 'Desligar')
        #portao_message_var = False
    elif not lampada_message_var:
        client.publish("/Controlador/Lampadas/L1", 'Ligar')
        #portao_message_var = True

#=========VARIÁVEIS GLOBAIS===========
temperatura_message_sala_var = '0'
temperatura_message_quarto_var = '0'
umidade_message_var = '0'
portao_message_var = False
lampada_message_var = False
#=========FIM VARIÁVEIS GLOBAIS===========

client = paho.mqtt.client.Client(client_id='1', clean_session=False)
client.connect(host='192.168.25.7', port=1883)
    
client.on_connect = on_connect
client.message_callback_add('/Temperatura/Sala', on_message_temperatura_sala)
client.message_callback_add('/Temperatura/Quarto', on_message_temperatura_quarto)
client.message_callback_add('/Portao', on_message_portao)
client.message_callback_add('/Umidade/Sala', on_message_umidade)
client.message_callback_add('/Lampadas/L1', on_message_lampada)
client.on_message = on_message

def main():
    
    root = Tk()
    #============================TEMPERATURA SALA===================================
    temperatura_sala = Frame(root, highlightbackground="blue",highlightthickness=2, padx=20, pady=20)
    temperatura_sala.pack(side=LEFT)

    temperatura_title_sala = Label(temperatura_sala, text='Temperatura da Sala')
    temperatura_title_sala["font"] = ("Helvetica", "14", "bold")
    temperatura_title_sala.pack()

    temperatura_message_sala = Label(temperatura_sala, text='Valor do Sensor')
    temperatura_message_sala["font"] = ("Helvetica", "12")
    temperatura_message_sala.pack()
    #============================FIM TEMPERATURA SALA================================

    #============================TEMPERATURA QUARTO===================================
    temperatura_quarto = Frame(root, highlightbackground="blue",highlightthickness=2, padx=20, pady=20)
    temperatura_quarto.pack(side=LEFT)

    temperatura_title_quarto = Label(temperatura_quarto, text='Temperatura do Quarto')
    temperatura_title_quarto["font"] = ("Helvetica", "14", "bold")
    temperatura_title_quarto.pack()

    temperatura_message_quarto = Label(temperatura_quarto, text='Valor do Sensor')
    temperatura_message_quarto["font"] = ("Helvetica", "12")
    temperatura_message_quarto.pack()
    #============================FIM TEMPERATURA QUARTO================================

    #============================SENSOR DE UMIDADE================================================
    umidade = Frame(root, highlightbackground="blue",highlightthickness=2, padx=20, pady=20)
    umidade.pack(side=LEFT)

    umidade_title = Label(umidade, text='Umidade da Sala')
    umidade_title["font"] = ("Helvetica", "14", "bold")
    umidade_title.pack()

    umidade_message = Label(umidade, text='Valor do Sensor')
    umidade_message["font"] = ("Helvetica", "12")
    umidade_message.pack()
    #============================FIM SENSOR DE UMIDADE============================================

    #============================PORTAO================================================
    portao = Frame(root, highlightbackground="blue",highlightthickness=2,padx=20, pady=20)
    portao.pack(side=BOTTOM)

    portao_title = Label(portao, text='Portão da Frente')
    portao_title["font"] = ("Helvetica", "14", "bold")
    portao_title.pack()

    portao_message = Label(portao, text='Valor do Sensor')
    portao_message["font"] = ("Helvetica", "12")
    portao_message.pack()

    portao_button = Button(portao)
    portao_button["text"] = "Abrir!"
    portao_button["font"] = ("Helvetica", "10")
    portao_button["width"] = 7
    portao_button["command"] = on_button_portao
    portao_button.pack(side=BOTTOM) 
    #============================FIM PORTAO============================================

    #============================LAMPADA================================================
    lampada = Frame(root, highlightbackground="blue",highlightthickness=2,padx=20, pady=20)
    lampada.pack(side=BOTTOM)

    lampada_title = Label(lampada, text='Lampada')
    lampada_title["font"] = ("Helvetica", "14", "bold")
    lampada_title.pack()

    lampada_message = Label(lampada, text='Valor do Sensor')
    lampada_message["font"] = ("Helvetica", "12")
    lampada_message.pack()

    lampada_button = Button(lampada)
    lampada_button["text"] = "Ligar!"
    lampada_button["font"] = ("Helvetica", "10")
    lampada_button["width"] = 7
    lampada_button["command"] = on_button_lampada
    lampada_button.pack(side=BOTTOM) 
    #============================FIM LAMPADA============================================

    while True:
        root.update()
        client.loop(.1)
        temperatura_message_sala.configure(text=temperatura_message_sala_var)
        temperatura_message_quarto.configure(text=temperatura_message_quarto_var)
        umidade_message.configure(text=umidade_message_var)

        if portao_message_var:
            portao_message.configure(text='Portão Aberto')
            portao_button.configure(text='Fechar!')
        elif not portao_message_var:
            portao_message.configure(text='Portão Fechado')
            portao_button.configure(text='Abrir!')

        if lampada_message_var:
            lampada_message.configure(text='Lâmpada Ligada')
            lampada_button.configure(text='Desligar!')
        elif not lampada_message_var:
            lampada_message.configure(text='Lâmpada Desligada')
            lampada_button.configure(text='Ligar!')

if __name__ == '__main__':
	main()
	sys.exit(0)
