import datetime
import socket

import pyautogui

import time


def conectar():
    # Buscamo o Socket e passado a informação que vamos utlizar o protocolo TCP/IP no modo de Stream
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Realiza a conexão com o servidor que esta escultando.
    cliente.connect(("127.0.0.1", 8989))

    # Chamamos um input para informar uma mensagem para ser transmitida.
    mensagem = input("Mensagem para ser transmitida para o servidor: ")

    # Enviamos a mensagem informada via conexão estabelecida e codificando ela para ser transmitida.
    cliente.send(mensagem.encode())

    print("Mensagem enviada!")

    # Fechando a conexão

    cliente.close()


def print_tela():
    # Usamos o pyautogui para obter um print da tela do cliente
    img = pyautogui.screenshot()
    # Obtemos aqui a data/hora para aplicar como o nome do arquivo do screenprint.
    nome_arquivo = datetime.datetime.now()
    nome_arquivo = str(nome_arquivo)
    nome_arquivo = nome_arquivo.replace(':', '').replace('.', '').replace('-', '').replace(' ', '')
    img.save(f"{nome_arquivo}.tmp")


while True:
    conectar()


