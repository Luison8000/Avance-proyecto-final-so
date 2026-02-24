def procesar_comando(comando):
    global usuario_autenticado

    if comando.startswith("LOGIN:"):
        datos = comando.split(":")
        usuario = datos[1]
        password = datos[2]

        if autenticar(usuario, password):
            usuario_autenticado = True
            return "LOGIN_OK"
        else:
            return "LOGIN_FAIL"

    if not usuario_autenticado:
        return "ERROR: No autenticado"

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
