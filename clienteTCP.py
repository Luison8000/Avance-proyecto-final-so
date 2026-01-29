import socket

ip = "127.0.0.1"
puerto = 5000

while True:
    cmd = input(">> ")

    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((ip, puerto))
    c.send(cmd.encode())
    print(c.recv(4096).decode())
    c.close()
