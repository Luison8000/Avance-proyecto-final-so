import socket

HOST = "127.0.0.1"
PORT = 5000


def enviar_comando(comando):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORT))

    cliente.send(comando.encode())
    respuesta = cliente.recv(4096).decode()

    cliente.close()
    return respuesta


def mostrar_menu():
    print("\n--- CLIENTE DE PROCESOS ---")
    print("1. Listar procesos")
    print("2. Iniciar proceso")
    print("3. Detener proceso")
    print("4. Ver estado sistema")
    print("5. Salir")


def main():
    opcion = ""

    while opcion != "5":
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print(enviar_comando("LIST"))

        elif opcion == "2":
            nombre = input("Comando a ejecutar: ")
            print(enviar_comando(f"START:{nombre}"))

        elif opcion == "3":
            pid = input("PID a detener: ")
            print(enviar_comando(f"STOP:{pid}"))

        elif opcion == "4":
            print(enviar_comando("STATUS"))

        elif opcion == "5":
            print("Saliendo...")

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
