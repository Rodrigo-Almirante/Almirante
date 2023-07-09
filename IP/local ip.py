import socket

# Get the local IP address
ip_address = socket.gethostbyname(socket.gethostname())

# Print the IP address obtained 
print("IP Local: ",ip_address)

