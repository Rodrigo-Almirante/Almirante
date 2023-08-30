import uuid

# print (hex(uuid.getnode()))

mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elementos) & 0xff) for elementos in range(0,8*6,8)][::-1])
print("La direccion MAC es:", mac_address)




