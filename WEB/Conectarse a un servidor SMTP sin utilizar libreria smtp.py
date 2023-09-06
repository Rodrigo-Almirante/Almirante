import socket

def enviar_correo(destinatario, asunto, mensaje):
    # Configurar los detalles del servidor SMTP
    servidor_smtp = "smtp.example.com"
    puerto_smtp = 25
    usuario_smtp = "tu_usuario"  # Opcional
    clave_smtp = "tu_clave"     # Opcional

    # Establecer la conexión con el servidor SMTP
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.connect((servidor_smtp, puerto_smtp))
    respuesta = servidor.recv(1024).decode()
    print(respuesta)

    # Enviar el nombre de usuario (opcional)
    if usuario_smtp:
        servidor.send(f"EHLO {usuario_smtp}\r\n".encode())
        respuesta = servidor.recv(1024).decode()
        print(respuesta)

    # Autenticarse con el servidor (opcional)
    if clave_smtp:
        servidor.send(f"AUTH LOGIN\r\n".encode())
        respuesta = servidor.recv(1024).decode()
        print(respuesta)
        servidor.send(f"{usuario_smtp}\r\n".encode())
        respuesta = servidor.recv(1024).decode()
        print(respuesta)
        servidor.send(f"{clave_smtp}\r\n".encode())
        respuesta = servidor.recv(1024).decode()
        print(respuesta)

    # Enviar el remitente
    servidor.send(f"MAIL FROM:<{usuario_smtp}>\r\n".encode())
    respuesta = servidor.recv(1024).decode()
    print(respuesta)

    # Enviar el destinatario
    servidor.send(f"RCPT TO:<{destinatario}>\r\n".encode())
    respuesta = servidor.recv(1024).decode()
    print(respuesta)

    # Iniciar el cuerpo del mensaje
    servidor.send("DATA\r\n".encode())
    respuesta = servidor.recv(1024).decode()
    print(respuesta)

    # Enviar el mensaje
    servidor.send(f"Subject:{asunto}\r\n\r\n{mensaje}\r\n.\r\n".encode())
    respuesta = servidor.recv(1024).decode()
    print(respuesta)

    # Cerrar la conexión con el servidor SMTP
    servidor.send("QUIT\r\n".encode())
    respuesta = servidor.recv(1024).decode()
    print(respuesta)
    servidor.close()

# Ejemplo de uso
destinatario = "correo_destino@example.com"
asunto = "Prueba de correo"
mensaje = "Este es un mensaje de prueba enviado desde Python"

enviar_correo(destinatario, asunto, mensaje)
