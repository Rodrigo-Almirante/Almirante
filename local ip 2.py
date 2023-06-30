import socket

# Leer hostname 
#hostname = socket.gethostname()
hostname = socket.gethostbyname("google.com")

# Tomar la direccion IP relacionada a hostname
ip_address = socket.gethostbyname(hostname)

# Imprimir la direccion IP obtenida
print("Direccion IP: {}".format(ip_address))
