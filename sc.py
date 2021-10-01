import datetime

import socket

import pyautogui


def conectar():
    while True:

        # Busca o Socket e passa a informação que vamos utlizar o protocolo TCP/IP no modo de Stream
        conect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Buscamos o codigo do staus do servidor
        status_servidor = conect.connect_ex(("127.0.0.1", 8989))

        if status_servidor == 10061:
            print("Tentando conexão!")
        else:
            print("Conectado!")
            # Recebendo solicitação do servidor do printscreen
            recebe = conect.recv(1024)
            # Recebendo o comando disparado pelo servidor
            comando = recebe.decode().upper()
            # Aqui verificamos o comando recebido pelo servidor
            if comando == "S":
                print_tela(conect)
                conect.close()
            elif comando == "N":
                print("Servidor foi desligado")
                conect.close()
            elif comando != "S" or comando != "N":
                print("Comando não reconhecido")
                conect.close()


def print_tela(clt):

    # Usamos o pyautogui para obter um print da tela do cliente
    img = pyautogui.screenshot()
    # Obtemos aqui a data/hora para aplicar como o nome do arquivo do screenprint.
    nome_arquivo = datetime.datetime.now()
    nome_arquivo = str(nome_arquivo)
    nome_arquivo = nome_arquivo.replace(':', '').replace('.', '').replace('-', '').replace(' ', '')
    img.save(f"{nome_arquivo}.jpg")
    # Aqui nos vamos transmitir o printscreen para o servidor.
    arquivo = open(nome_arquivo + ".jpg", 'rb')
    ler = arquivo.read(2048)
    # Se não percorrer o arquivo com o while ele vai enviar apenas os primeiros bytes do arquivo.
    while ler:
        clt.send(ler)
        ler = arquivo.read(2048)
    arquivo.close()

    print("Printscreen enviado!")


conectar()
