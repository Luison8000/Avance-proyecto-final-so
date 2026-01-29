import psutil
import subprocess
import os
import signal

def ver_procesos():
    print("\nPID | Nombre | CPU% | RAM%")
    print("-" * 30)
    for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            info = p.info
            print(f"{info['pid']} | {info['name'][:10]} | {info['cpu_percent']} | {info['memory_percent']:.2f}")
        except:
            pass

def arrancar(cmd):
    subprocess.Popen(cmd.split())
    print(" Proceso arrancado")

def matar(pid):
    os.kill(pid, signal.SIGTERM)
    print(" Proceso terminado")

def estado_pc():
    print(f" CPU: {psutil.cpu_percent()}%")
    print(f" RAM: {psutil.virtual_memory().percent}%")

while True:
    print("\n1) Ver procesos")
    print("2) Arrancar programa")
    print("3) Matar proceso")
    print("4) Estado del sistema")
    print("5) Salir")

    op = input("¿Qué hacemos?: ")

    if op == "1":
        ver_procesos()
    elif op == "2":
        comando = input("Comando: ")
        arrancar(comando)
    elif op == "3":
        pid = int(input("PID: "))
        matar(pid)
    elif op == "4":
        estado_pc()
    elif op == "5":
        print("Bye")
        break
