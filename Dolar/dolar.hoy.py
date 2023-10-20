import requests
from colorama import just_fix_windows_console          # pip install colorama

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


  numero1=float(Oficial)
  numero2=float(Blue)
  #print(numero1,numero2)

  diferencia = numero2 - numero1
  # print("Diferencia: ",diferencia)
  Brecha = (diferencia / numero1) * 100

  return Brecha

conectado=False

just_fix_windows_console()                             # Arregla los colores ANSI para la consola de Windows

try:

# Dolar Blue

  url = 'https://dolarhoy.com/'
  response = requests.get(url)

  if response.status_code == 200:
    conectado = True

    print("\nCotizacion del dolar sitio dolarhoy.com")
    start = response.text.find('Compra') + len('</div><div class="val">')+7

    if start <= 80:
     print("\nString "+color.PURPLE+"Compra",color.END+"NO Encontrada")

    else:
     end = response.text.find('</div></div>', start)
     compra = response.text[start:end]
     print("\nBlue COMPRA    : $"+compra)

    start = response.text.find('Venta') + len('</div><div class="val">$')+5

    if start <= 80:
     print("\nString "+color.PURPLE+"Venta",color.END+"NO Encontrada")

    else:
     end = response.text.find('</div></div>', start)
     venta = response.text[start:end]
     print("Blue VENTA     : "+color.CYAN+"$"+venta+ color.END)

     Blue=venta

  else:
    print("No se pudo conectar al website.")

# Dolar Banco Nacion

  url = 'https://dolarhoy.com/'
  response = requests.get(url)

  if response.status_code == 200:
    conectado = True

    start = response.text.find('oficial promedio') + len('</a><div class="values"><div class="compra"><div class="label">Compra</div><div class="val">')+len('348.96')+11
    ValorOficialPromedio=start

    if start <= 80:
     print("\nString "+color.RED+"Compra",color.END+"NO Encontrada")

    else:
     end = response.text.find('</div></div>', start)
     compra = response.text[start:end]
     print("\nOficial COMPRA : $"+compra)

    start = len('</div></div><div class="venta"><div class="label">Venta</div><div class="val">')+len('$368.60')+ValorOficialPromedio

    if start <= 80:
     print("\nString "+color.RED+"Venta",color.END+"NO Encontrada")

    else:
     end = response.text.find('</div></div>', start)
     venta = response.text[start:end]
     #print(start, end,venta)
     print("Oficial VENTA  : $"+venta)

    Oficial=venta

  else:
    print("No se pudo conectar al website.")

  # print("Valores:",Oficial,Blue)

  Brecha=CalcularBrecha(Oficial,Blue)
  print("\nBrecha         : "+color.RED+"%"+str(Brecha),color.END,"\n")

 
  dolar2019="69.00"
  Brecha=CalcularBrecha(dolar2019,Blue)

  print(color.BOLD+"Devaluacion desde 2019 : "+color.END+color.CYAN+"%"+str(int(Brecha)),color.END)

  conectado=True

except:
 if(conectado==False):
  print("\n"+color.PURPLE+"Sin conexion",color.END)

input("\nPersione enter para continuar...")