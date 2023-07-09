import socket

# Tomar la direccion IPv6
ipv6 = socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET6)[0][4][0]

# Imprimir
print("La direccion IPv6 actual es:", ipv6)
