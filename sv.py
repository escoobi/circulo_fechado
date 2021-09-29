import socket

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind((socket.gethostname(), 8989))
ss.listen(5)
