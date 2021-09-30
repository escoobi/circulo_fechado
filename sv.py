import socket


def main():
    # Buscamo o Socket e passado a informação que vamos utlizar o protocolo TCP/IP no modo de Stream
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Essa é show... quando damos um quit no script ele para de escultar a conexao. Isso ajuda quando tem algum crash e iniciamos a aplicação novamente.
    ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Passammos as informações de porta e endereço que vamos ficar escultando.
    ss.bind(("localhost", 8989))

    # Vamos escultar 10 conexões
    ss.listen(10)

    print("Aguardando conexão!!!")

    while True:
        # Aceitamos as conexões e passamos as informações recebidas do cliente
        conexao, cliente = ss.accept()

        escultar(conexao, cliente)


def escultar(conexao, cliente):
    with conexao:
        print("Conectado com: ", cliente[0])
        while True:

            # Recebendo do dados passados com a conexão estabelecida, temos que informar o tamanho do byffer a ser transpotado, no caso 1024 bytes
            recebe = conexao.recv(1024)
            if not recebe:
                break
            # A mensagem transmitida codificada e usamos o decode para poder abrir ela.
            print(recebe.decode())


main()

