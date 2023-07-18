# coding: cp1252                                                 # Se tiene que utilizar por los acentos en el codigo, incluso en los comentarios
# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

def obtener_pronostico_semana(localidad):
    # Localidad = 11221
    url = "https://www.accuweather.com/en/ar/santa-fé/11221/daily-weather-forecast/11221"


    # Establecer encabezados para hacer que parezca que se está usando Firefox 115
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0',
    }

    # Realizar la solicitud HTTP a la página de búsqueda de la localidad
    response = requests.get(url, headers=headers)


    # Analizar el contenido HTML de la respuesta
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar el enlace del pronóstico semanal en la página de resultados de búsqueda
    resultado = soup.find(class_='daily-wrapper').find('a')

    pronostico_url = f'https://www.accuweather.com{resultado["href"]}'
    url_now = pronostico_url.split('?')[0]                                 # Corta la string cuando encuentra ?

    # Realizar la solicitud HTTP al enlace del pronóstico semanal
    response = requests.get(url_now, headers=headers)                     # Utiliza la string cortada

    dia = soup.find_all('span', attrs={'module-header dow date'})    
    tabla_dia=list()
    for span in dia:
      tabla_dia.append(span.get_text().strip())


    fecha = soup.find_all('span', attrs={'module-header sub date'})

    tabla_fecha=list()
    for span in fecha:
      tabla_fecha.append(span.get_text().strip())

    alta = soup.find_all('span', attrs={'high'})
    tabla_alta=list()
    for span in alta:
      tabla_alta.append(span.get_text().strip())

    baja = soup.find_all('span', attrs={'low'})
    tabla_baja=list()
    for span in baja:
      tabla_baja.append(span.get_text().strip())

    realfeel = soup.find_all(class_='panel-item', attrs={'value'})
    tabla_realfeel=list()
    for span in realfeel:
      tabla_realfeel.append(span.get_text().strip())


    estado = soup.find_all(class_='phrase')
    tabla_estado=list()
    for span in estado:
      tabla_estado.append(span.get_text().strip())

    print("\nDia", "Fecha", "Temp", "   Extra\n")

    for i, alta in enumerate(tabla_alta):
     print(tabla_dia[i], tabla_fecha[i], tabla_alta[i],tabla_baja[i],tabla_realfeel[i],tabla_estado[i])

    return


# Ingresar la localidad
#localidad = input("Ingrese la localidad: ")
localidad = 11221

# Obtener el pronóstico de la semana para la localidad ingresada
pronosticos_semana = obtener_pronostico_semana(localidad)

