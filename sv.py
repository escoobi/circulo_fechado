import datetime
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
    print("Conectado com: ", cliente[0])
    # Enviamos a mensagem informada via conexão estabelecida e codificando ela para ser transmitida.
    mensagem = input("Soliciar prinscreen cliente: S(Sim) ou N(Não)? ")
    conexao.send(mensagem.encode())
    if mensagem.upper() == "S":
        print("Solicitadação enviada!")
        nome_arquivo = datetime.datetime.now()
        nome_arquivo = str(nome_arquivo)
        nome_arquivo = str(nome_arquivo)
        nome_arquivo = nome_arquivo.replace(':', '').replace('.', '').replace('-', '').replace(' ', '')
        abrir = open(f"r_{nome_arquivo}.jpg", "wb")
        # Recebendo do dados passados com a conexão estabelecida, temos que informar o tamanho do byffer a ser transpotado, no caso 1024 bytes
        recebe = conexao.recv(2048)
        # Se não percorrer o arquivo com o while ele vai enviar apenas os primeiros bytes do arquivo.
        while recebe:
            abrir.write(recebe)
            recebe = conexao.recv(2048)
        print("Printscreen recebido com sucesso!")
        abrir.close()
    elif mensagem.upper() == "N":
        conexao.close()
        quit()
    elif mensagem.upper() != "N" or mensagem.upper() != "S":
        print("Comando não aceito.")


main()

