import requests                                                   # pip install requests
import json                                                       # build-in

print("\nValor del dolar cotizacion actual\n")

# Hacer una solicitud GET a la URL
respuesta = requests.get("https://www.dolarsi.com/api/api.php?type=dolar")

# Obtener el contenido de la respuesta en formato JSON
contenido = respuesta.json()

#print(contenido)
#print(json.dumps(contenido, indent=4))


print("Compra",contenido[1]['casa']['nombre'],": $"+contenido[1]['casa']['compra'])
print("Venta ",contenido[1]['casa']['nombre'],": $"+contenido[1]['casa']['venta'])