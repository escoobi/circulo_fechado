import socket


def conectar():
    # Buscamo o Socket e passado a informação que vamos utlizar o protocolo TCP/IP no modo de Stream
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Realiza a conexão com o servidor que esta escultando.
    cliente.connect(("127.0.0.1", 8989))

    # Chamamos um input para informar uma mensagem para ser transmitida.
    mensagem = input("Mensagem para ser transmitira para o servidor: ")

    # Enviamos a mensagem informada via conexão estabelecida e codificando ela para ser transmitida.
    cliente.send(mensagem.encode())

    print("Mensagem enviada!")

    # Fechando a conexão

    cliente.close()


conectar()
