

# Proyecto de Redes, Seguridad y Sistemas Distribuidos en Red Hat Enterprise Linux

---

# PARTE 1 — Diseño y Configuración de Red

## 1. Verificación del entorno

```bash
uname -a
````

```bash
ip a
```

---

## 2. Configuración de la red interna

Se utilizan dos máquinas virtuales RHEL conectadas mediante red interna en VirtualBox.

Direcciones IP:

* Servidor: 192.168.100.10
* Cliente: 192.168.100.20
* Máscara: 255.255.255.0

---

## 3. Configuración de IP estática

### 3.1 Editar interfaz de red

```bash
sudo nano /etc/sysconfig/network-scripts/ifcfg-enp0s3
```

### 3.2 Configuración en servidor

```
BOOTPROTO=none
IPADDR=192.168.100.10
PREFIX=24
ONBOOT=yes
```

### 3.3 Configuración en cliente

```
BOOTPROTO=none
IPADDR=192.168.100.20
PREFIX=24
ONBOOT=yes
```

### 3.4 Reiniciar servicio de red

```bash
sudo systemctl restart NetworkManager
```

---

## 4. Verificación de conectividad

```bash
ping 192.168.100.10
```

```bash
ping 192.168.100.20
```

```bash
traceroute 192.168.100.10
```

Se verifica conectividad sin pérdida de paquetes.

---

# PARTE 2 — Implementación de Servicios de Red

## 1. Instalación de servicios

```bash
sudo dnf install openssh-server httpd -y
```

---

## 2. Activación de servicios

```bash
sudo systemctl enable sshd
sudo systemctl start sshd
```

```bash
sudo systemctl enable httpd
sudo systemctl start httpd
```

---

## 3. Creación de página web de prueba

```bash
echo "Servidor web funcionando correctamente" | sudo tee /var/www/html/index.html
```

---

## 4. Prueba de servicios

Acceso SSH:

```bash
ssh usuario@192.168.100.10
```

Acceso web:

```
http://192.168.100.10
```

---

# PARTE 3 — Seguridad en la Red

## 1. Configuración de firewall

```bash
sudo systemctl enable firewalld
sudo systemctl start firewalld
```

```bash
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
```

---

## 2. Autenticación SSH mediante clave

### 2.1 Generación de claves

```bash
ssh-keygen
```

### 2.2 Copiar clave al servidor

```bash
ssh-copy-id usuario@192.168.100.10
```

---

## 3. Deshabilitar autenticación por contraseña

```bash
sudo nano /etc/ssh/sshd_config
```

Cambiar:

```
PasswordAuthentication no
```

Reiniciar servicio:

```bash
sudo systemctl restart sshd
```

---

## 4. Configuración de HTTPS

### 4.1 Instalación de SSL

```bash
sudo dnf install mod_ssl -y
```

### 4.2 Generación de certificado

```bash
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
-keyout /etc/pki/tls/private/apache.key \
-out /etc/pki/tls/certs/apache.crt
```

### 4.3 Reiniciar Apache

```bash
sudo systemctl restart httpd
```

Acceso:

```
https://192.168.100.10
```

---

# PARTE 4 — Análisis de Seguridad

## 1. Escaneo de puertos

```bash
nmap 192.168.100.10
```

---

## 2. Auditoría del sistema

```bash
sudo dnf install lynis -y
sudo lynis audit system
```

---

# PARTE 5 — Sistema de Archivos Distribuido (NFS)

## 1. Configuración en servidor

```bash
sudo dnf install nfs-utils -y
sudo mkdir /shared
sudo chmod 777 /shared
```

```bash
echo "/shared 192.168.100.0/24(rw,sync,no_root_squash)" | sudo tee -a /etc/exports
```

```bash
sudo systemctl enable nfs-server
sudo systemctl start nfs-server
sudo exportfs -r
```

---

## 2. Configuración en cliente

```bash
sudo dnf install nfs-utils -y
sudo mkdir /mnt/shared
```

```bash
sudo mount 192.168.100.10:/shared /mnt/shared
```

---

## 3. Prueba de funcionamiento

```bash
touch /mnt/shared/prueba.txt
```

Se verifica acceso compartido entre ambas máquinas.

---

# PARTE 6 — Modelo Peer-to-Peer (P2P)

## 1. Instalación de cliente BitTorrent

```bash
sudo dnf install transmission -y
```

---

## 2. Prueba de transferencia

* Crear archivo en una máquina
* Generar torrent
* Descargar desde la segunda máquina

Se verifica comunicación P2P dentro de la red local.

---

# PARTE 7 — Resultados

Se obtuvieron los siguientes resultados:

* Conectividad de red exitosa
* Acceso remoto SSH funcional
* Servidor web HTTP y HTTPS operativo
* Firewall configurado correctamente
* Autenticación segura mediante claves
* Compartición de archivos mediante NFS
* Transferencia P2P funcional

---


