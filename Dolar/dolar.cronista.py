import requests

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


# Funcion Calcula Brecha, calcula la brecha entre el dolar oficial y el blue devolviendo un valor flotante
def CalcularBrecha(Oficial,Blue):

  numero1=int(Oficial.split(",")[0],10)
  numero2=int(Blue.split(",")[0],10)

  diferencia = numero2 - numero1
  Brecha = (diferencia / numero1) * 100

  return Brecha


# Dolar Blue
url = 'https://www.cronista.com/MercadosOnline/moneda.html?id=ARSB'

response = requests.get(url)

if response.status_code == 200:

    print("\nCotizacion del dolar Blue del sitio cronista.com")
    start = response.text.find('Compra') + len('</div><div class=buy-value><span class="currency">$</span>')+len('517,00')
    end = response.text.find('</div></div></a></td>', start)
    compra = response.text[start:end]
    #print(start, end,compra)
    print("\nPrecio del dolar Blue COMPRA : $"+compra)

    start = response.text.find('Venta') + len('</div><div class=sell-value><span class="currency">$</span')+len('522,00')
    end = response.text.find('</div></div></a></td>', start)
    venta = response.text[start:end]
    #print(start, end,venta)
    print("Precio del dolar Blue VENTA  : "+color.CYAN+"$"+venta+ color.END)

    Blue=venta

else:
    print("No se pudo conectar al website.")


# Dolar Banco Nacion

url = 'https://www.cronista.com/MercadosOnline/moneda.html?id=ARS'

response = requests.get(url)

if response.status_code == 200:

    start = response.text.find('Compra') + len('</div><div class=buy-value><span class="currency">$</span>')+len('264,00')
    end = response.text.find('</div></div></a></td>', start)
    compra = response.text[start:end]
    #print(start, end,compra)
    print("\nPrecio del dolar BNA COMPRA : $"+compra)

    start = response.text.find('Venta') + len('</div><div class=sell-value><span class="currency">$</span')+len('522,00')
    end = response.text.find('</div></div></a></td>', start)
    venta = response.text[start:end]
    #print(start, end,venta)
    print("Precio del dolar BNA VENTA  : $"+venta)

    Oficial=venta

else:
    print("No se pudo conectar al website.")

Brecha=CalcularBrecha(Oficial,Blue)
#print(Brecha)
print("\nBrecha: "+color.RED+"%"+str(Brecha),color.END)
