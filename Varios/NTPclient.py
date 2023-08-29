import socket
import struct
import time
import ctypes


server="pool.ntp.org"
NTP_PACKET_FORMAT = "!12I"
NTP_DELTA = 2208988800  # Valor de desplazamiento de fecha y hora entre NTP y POSIX Epoch

# Crear un socket UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enviar solicitud de tiempo NTP al servidor
address = (server, 123)
data = b'\x1b' + 47 * b'\0'
client.sendto(data, address)

# Esperar respuesta del servidor
data, _ = client.recvfrom(1024)

# Extraer el timestamp de la respuesta del servidor
unpacked_data = struct.unpack(NTP_PACKET_FORMAT, data[0:struct.calcsize(NTP_PACKET_FORMAT)])
ntp_timestamp = unpacked_data[10] + float(unpacked_data[11]) / 2**32

# Calcular el timestamp POSIX a partir del timestamp NTP
posix_timestamp = ntp_timestamp - NTP_DELTA

#print(posix_timestamp)

# Establecer la hora del sistema utilizando el timestamp POSIX calculado
#print(time.ctime(posix_timestamp))

# Cerrar el socket
client.close()

# ctypes.windll.kernel32.SetSystemTime(time.ctime(posix_timestamp))

print("Hora recibida exitosamente del servidor NTP! :", time.ctime(posix_timestamp))


