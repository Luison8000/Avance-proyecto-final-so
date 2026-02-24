import socket
import json

HOST = "0.0.0.0"
PORT = 6000

# Servidores disponibles
SERVIDORES = [
    {"host": "127.0.0.1", "port": 5000},
    {"host": "127.0.0.1", "port": 5001}
]

indice_servidor = 0


def enviar_a_servidor(comando):
    global indice_servidor

    servidor = SERVIDORES[indice_servidor]

    # Round Robin
    indice_servidor = (indice_servidor + 1) % len(SERVIDORES)

    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((servidor["host"], servidor["port"]))
        cliente.send(comando.encode())
        respuesta = cliente.recv(4096).decode()
        cliente.close()
        return respuesta
    except Exception as e:
        return f"Error conectando con servidor {servidor['port']}: {e}"


def iniciar_middleware():
    middleware = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    middleware.bind((HOST, PORT))
    middleware.listen()

    print(f"Middleware escuchando en puerto {PORT}...")

    while True:
        conn, addr = middleware.accept()
        print(f"Cliente conectado desde {addr}")

        comando = conn.recv(4096).decode()
        respuesta = enviar_a_servidor(comando)

        conn.send(respuesta.encode())
        conn.close()


if __name__ == "__main__":
    iniciar_middleware()
