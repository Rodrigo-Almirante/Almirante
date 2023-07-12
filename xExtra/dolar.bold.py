import requests                                                   # pip install requests
import json                                                       # build-in

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

print("\nValor del dolar cotizacion actual\n")

# Hacer una solicitud GET a la URL
respuesta = requests.get("https://www.dolarsi.com/api/api.php?type=dolar")

# Obtener el contenido de la respuesta en formato JSON
contenido = respuesta.json()

#print(contenido)
#print(json.dumps(contenido, indent=4))


print("Compra",contenido[1]['casa']['nombre'],": $"+contenido[1]['casa']['compra'])
print(color.BOLD +"Venta ",contenido[1]['casa']['nombre'],": $"+contenido[1]['casa']['venta']+ color.END)