import socket

print("IPv6 de google resuelta: ",socket.gethostbyaddr('2001:4860:4860::8888')[0])

#print("IPv6 de google resuelta: ",socket.gethostbyaddr('2800:1008:4002:812::2004')[0])

# Toma la direccion IPv6 de www.google.com
try:
    google_ip = socket.getaddrinfo('www.google.com', None, socket.AF_INET6)[0][4][0]
    print("\nLa direccion IPv6 de www.google.com is:", google_ip)
except socket.gaierror:
    print("Error al resolver la direccion IPv6 de google.com")

