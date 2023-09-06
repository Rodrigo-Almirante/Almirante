import smtplib

def enviar_correo(destinatario, asunto, mensaje):
    # Configurar los detalles del servidor SMTP
    servidor_smtp = "smtp.example.com"
    puerto_smtp = 587
    usuario_smtp = "tu_usuario"
    clave_smtp = "tu_clave"

    # Establecer la conexión con el servidor SMTP
    servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
    servidor.starttls()
    servidor.login(usuario_smtp, clave_smtp)

    # Crear el mensaje de correo
    mensaje_correo = f"Subject: {asunto}\n\n{mensaje}"

    # Enviar el correo
    servidor.sendmail(usuario_smtp, destinatario, mensaje_correo)

    # Cerrar la conexión con el servidor SMTP
    servidor.quit()

# Ejemplo de uso
destinatario = "correo_destino@example.com"
asunto = "Prueba de correo"
mensaje = "Este es un mensaje de prueba enviado desde Python"

enviar_correo(destinatario, asunto, mensaje)
