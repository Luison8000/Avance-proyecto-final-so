import socket
import os
import psutil
import subprocess
import signal

HOST = "0.0.0.0"
PORT = 5000


def listar_procesos():
    procesos = []
    for proceso in psutil.process_iter(['pid', 'name']):
        try:
            pid = proceso.info['pid']
            nombre = proceso.info['name']
            procesos.append(f"{pid} - {nombre}")
        except:
            pass
    return "\n".join(procesos)


def iniciar_proceso(nombre):
    try:
        proceso = subprocess.Popen(nombre.split())
        return f"Proceso iniciado con PID {proceso.pid}"
    except Exception as e:
        return f"Error: {e}"


def detener_proceso(pid):
    try:
        os.kill(int(pid), signal.SIGTERM)
        return "Proceso detenido correctamente"
    except Exception as e:
        return f"Error: {e}"


def estado_sistema():
    cpu = psutil.cpu_percent(interval=1)
    memoria = psutil.virtual_memory().percent
    return f"CPU: {cpu}% | Memoria: {memoria}%"


def procesar_comando(comando):
    if comando == "LIST":
        return listar_procesos()
    elif comando.startswith("START:"):
        nombre = comando.split(":")[1]
        return iniciar_proceso(nombre)
    elif comando.startswith("STOP:"):
        pid = comando.split(":")[1]
        return detener_proceso(pid)
    elif comando == "STATUS":
        return estado_sistema()
    else:
        return "Comando no reconocido"


def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen()

    print(f"Servidor escuchando en puerto {PORT}...")

    while True:
        conn, addr = servidor.accept()
        print(f"Conexión desde {addr}")

        datos = conn.recv(4096).decode()
        respuesta = procesar_comando(datos)

        conn.send(respuesta.encode())
        conn.close()


if __name__ == "__main__":
    iniciar_servidor()
