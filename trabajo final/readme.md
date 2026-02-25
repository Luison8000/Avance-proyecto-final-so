
# Sistema Distribuido para Administración Remota de Procesos
Implementación Segura con TLS y Panel Web

Autores:
- Minette Bibiana Hernández Velázquez
- Luis Martínez del Campo González
- Iñaki Covarrubias Bribiesca

---

## 1. Descripción del Proyecto

Este proyecto implementa un sistema cliente-servidor seguro para la administración remota de procesos en un entorno Linux (Red Hat).

El sistema permite:

- Listar procesos activos.
- Iniciar nuevos procesos.
- Finalizar procesos por PID.
- Monitorear uso de CPU y memoria.
- Autenticación de usuarios.
- Comunicación cifrada mediante TLS.
- Interfaz web desarrollada con Flask.

---

## 2. Requisitos del Sistema

### Software necesario

- Linux (probado en Red Hat)
- Python 3.10 o superior
- pip
- OpenSSL

### Librerías Python necesarias

Instalar con:

```bash
pip install psutil flask
````

---

## 3. Estructura del Proyecto

```
parte1_procesos/
│
├── servidor/
│   └── server.py
│
├── interfaz/
│   └── app.py
│
├── cliente/
│
├── usuarios.json
├── cert.pem
├── key.pem
└── README.md
```

---

## 4. Configuración Inicial

### 4.1 Crear archivo de usuarios

El archivo `usuarios.json` debe tener el siguiente formato:

```json
{
  "admin": "1234",
  "luis": "abcd"
}
```

---

### 4.2 Generar certificados TLS

Desde la carpeta raíz del proyecto:

```bash
openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout key.pem
```

Presionar Enter en todos los campos si no se desea personalizar.

---

## 5. Ejecución del Sistema

### Paso 1: Iniciar el servidor seguro

Desde la carpeta principal:

```bash
cd servidor
python3 server.py
```

El servidor escuchará en el puerto 5000.

---

### Paso 2: Iniciar la interfaz web

En otra terminal:

```bash
cd interfaz
python3 app.py
```

La aplicación web se ejecutará en:

```
http://localhost:7000
```

---

## 6. Funcionamiento

Al ingresar a la interfaz web se podrá:

* Visualizar el estado del sistema.
* Listar procesos activos.
* Iniciar procesos escribiendo el comando.
* Finalizar procesos ingresando el PID.

La comunicación entre la interfaz y el servidor está cifrada mediante TLS.

---

## 7. Protocolo de Comunicación

El servidor interpreta los siguientes comandos:

* LOGIN:usuario:contraseña
* LIST
* START:comando
* STOP:pid
* STATUS

---

## 8. Seguridad Implementada

* Autenticación basada en archivo JSON.
* Cifrado TLS mediante SSLContext.
* Protección contra interceptación de tráfico.
* Restricción de ejecución de comandos sin autenticación.

---

## 9. Problemas Comunes y Soluciones

### Error: Address already in use

Significa que el puerto 5000 está ocupado.

Solución:

```bash
lsof -i :5000
kill -9 <PID>
```

---

### Error: Connection refused

El servidor no está corriendo.

Verificar que `server.py` esté ejecutándose antes de iniciar Flask.

---

### Error TLS Handshake

Verificar que:

* Existan `cert.pem` y `key.pem`.
* El servidor esté ejecutándose en modo TLS.
* El cliente use `ssl.wrap_socket`.

---

## 10. Consideraciones Finales

Este sistema integra conceptos de:

* Sistemas Operativos
* Redes TCP/IP
* Seguridad informática
* Criptografía TLS
* Desarrollo Web
* Arquitectura Cliente-Servidor

El proyecto puede extenderse para:

* Implementar base de datos real.
* Agregar control de roles.
* Integrar balanceo de carga.
* Implementar autenticación más robusta.

