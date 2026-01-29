import socket
import psutil
import subprocess
import os
import signal

def manejar(cmd):
    if cmd == "LISTAR":
        texto = ""
        for p in psutil.process_iter(['pid', 'name']):
            texto += f"{p.info['pid']} - {p.info['name']}\n"
        return texto

    if cmd.startswith("INICIAR"):
        subprocess.Popen(cmd.split()[1:])
        return " Proceso iniciado"

    if cmd.startswith("DETENER"):
        pid = int(cmd.split()[1])
        os.kill(pid, signal.SIGTERM)
        return " Proceso muerto"

    if cmd == "ESTADO":
        return f"CPU {psutil.cpu_percent()}% | RAM {psutil.virtual_memory().percent}%"

    return "No entiendo pa"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("0.0.0.0", 5000))
sock.listen()

print(" Server prendido en puerto 5000")

while True:
    cliente, addr = sock.accept()
    cmd = cliente.recv(1024).decode().strip()
    print(f" {addr} -> {cmd}")
    resp = manejar(cmd)
    cliente.send(resp.encode())
    cliente.close()
