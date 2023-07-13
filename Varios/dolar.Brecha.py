import requests                                                   # pip install requests
import json                                                       # build-in
import socket                                                     # build-in

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# Funcion para verificar si hay conexion
def isConnectedWithInternet():
    try:
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False

# Funcion Calcula Brecha, calcula la brecha entre el dolar oficial y el blue devolviendo un valor flotante
def CalcularBrecha(Oficial,Blue):

  numero1=int(Oficial.split(",")[0],10)
  numero2=int(Blue.split(",")[0],10)

  diferencia = numero2 - numero1
  Brecha = (diferencia / numero1) * 100

  return Brecha

if isConnectedWithInternet()==True:                              # Llama a la funcion para ver si hay conexion a internet

   print("\nValor del dolar cotizacion actual\n")

   try:
     # Hacer una solicitud GET a la URL
     respuesta = requests.get("https://www.dolarsi.com/api/api.php?type=dolar")

     # Obtener el contenido de la respuesta en formato JSON
     contenido = respuesta.json()

     #print(json.dumps(contenido, indent=4))

     # Valor Oficial
     print("Compra",contenido[0]['casa']['nombre'],": $"+contenido[0]['casa']['compra'])
     print("Venta ",contenido[0]['casa']['nombre'],": $"+contenido[0]['casa']['venta'])

     # Valor Blue
     print("\nCompra",contenido[1]['casa']['nombre'],": $"+contenido[1]['casa']['compra'])
     print("Venta ",contenido[1]['casa']['nombre'],":"+color.CYAN,"$"+contenido[1]['casa']['venta']+ color.END)


     Oficial = contenido[0]['casa']['venta']
     Blue = contenido[1]['casa']['venta']

     Brecha=CalcularBrecha(Oficial,Blue)
     print("\nBrecha entre Oficial y Blue: "+color.RED+"% "+str(Brecha),color.END)

   except requests.exceptions.ConnectionError:
     print('\n\tNo se pudo conectar al website.')

else:
   print("\nNo hay conexion\n")
