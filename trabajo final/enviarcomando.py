def enviar_comando(comando):
    contexto = ssl.create_default_context()
    contexto.check_hostname = False
    contexto.verify_mode = ssl.CERT_NONE

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORT))

    cliente = contexto.wrap_socket(cliente, server_hostname=HOST)

    cliente.send(comando.encode())
    respuesta = cliente.recv(4096).decode()

    cliente.close()
    return respuesta
