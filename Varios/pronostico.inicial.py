# coding: cp1252
# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

def obtener_pronostico_semana(localidad):
    # Definir la URL de AccuWeather con la localidad
    #url = f'https://www.accuweather.com/es/search-locations?query={localidad}'
    url = "https://www.accuweather.com/en/ar/santa-f�/11221/daily-weather-forecast/11221"
    #print(url)

    # Establecer encabezados para hacer que parezca que se est� usando Firefox 115
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0',
    }

    # Realizar la solicitud HTTP a la p�gina de b�squeda de la localidad
    response = requests.get(url, headers=headers)
    #print("Respense text : \n",response.text)

    # Analizar el contenido HTML de la respuesta
    soup = BeautifulSoup(response.content, 'html.parser')
    #print("primer soup :\n",soup)

    # Encontrar el enlace del pron�stico semanal en la p�gina de resultados de b�squeda
    resultado = soup.find(class_='daily-wrapper').find('a')
    #print(resultado)
    pronostico_url = f'https://www.accuweather.com{resultado["href"]}'
    print(pronostico_url)
    url_now = pronostico_url.split('?')[0]                                 # Corta la string cuando encuentra ?
    print(url_now)

    # Realizar la solicitud HTTP al enlace del pron�stico semanal
    response = requests.get(url_now, headers=headers)                     # Utiliza la string cortada
    #response = requests.get(pronostico_url, headers=headers)
    #print("Response :\n",response.text)
    
    #start = response.text.find('module-header dow date') + len('<span class=') + len('Mon') + 9
    #end = start + 3


    #dia = response.text[start:end]
    #print(response.text)
    #print("PARA!!! ",start,end,dia)

    #pronostico_semana = soup.find_all(class_='info')

    #pronostico_semana = soup.find_all(class_='module-header dow date')
    #print("busca info: ",pronostico_semana)
    #dia = pronostico_semana.find(class_='date').get_text(strip=True)
    dia = soup.find_all('span', attrs={'module-header dow date'})
    #print(dia)
    #fecha = soup.find_all('span', attrs={'module-header sub date'})

    tabla_dia=list()
    for span in dia:
      #print(span.text)
      tabla_dia.append(span.get_text().strip())

    #for i, dia in enumerate(tabla_dia):
    # print(tabla_dia[i])

    fecha = soup.find_all('span', attrs={'module-header sub date'})
    #for span in fecha:
    #  print(span.text)

    tabla_fecha=list()
    for span in fecha:
      tabla_fecha.append(span.get_text().strip())

    #for i, fecha in enumerate(tabla_fecha):
    # print(tabla_dia[i], tabla_fecha[i])

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



    #print(dia)

    # Analizar el contenido HTML del pron�stico semanal
    soup = BeautifulSoup(response.content, 'html.parser')
    #print("Aca empieza: \n",soup)

    # Encontrar y extraer el pron�stico d�a por d�a de la semana
    #pronostico_semana = soup.find_all(class_='info')
    #pronostico_semana = soup.findAll('div', attrs={'class': 'half-day-card-header__content'})
    #pronostico_semana = soup.findAll('div', attrs={'class': 'half-day-card-header__title'})
    #pronostico_semana = soup.findAll('div', attrs={'class': 'half-day-card-content'})


    #print(pronostico_semana)

    # Crear una lista para almacenar los pron�sticos
    pronosticos = []

    # Recorrer los pron�sticos de cada d�a
    for pronostico_dia in pronostico_semana:
        # Extraer la informaci�n del pron�stico del d�a
        #dia = pronostico_dia.find(class_='short-date').get_text(strip=True)
        #print(soup)
        #descripcion = pronostico_dia.find(class_='phrase').get_text(strip=True)
        temperatura_max = pronostico_dia.find(class_='temperature').get_text(strip=True)
        #temperatura_min = pronostico_dia.find(class_='panel-item').get_text(strip=True)
        #print("Descripcion : ",descripcion)
        print("Max: ",temperatura_max)
        # Crear un diccionario con la informaci�n del pron�stico del d�a
        pronostico = {
            'D�a': dia,
            'Descripci�n': descripcion,
            'Temperatura m�xima': temperatura_max,
            'Temperatura m�nima': temperatura_min
        }

        # Agregar el pron�stico a la lista
        pronosticos.append(pronostico)

    
    return pronosticos


# Ingresar la localidad
#localidad = input("Ingrese la localidad: ")
localidad = 11221

# Obtener el pron�stico de la semana para la localidad ingresada
pronosticos_semana = obtener_pronostico_semana(localidad)

# Imprimir los pron�sticos d�a por d�a
#for pronostico in pronosticos_semana:
#    print(f'{pronostico["D�a"]}: {pronostico["Descripci�n"]}, {pronostico["Temperatura m�xima"]}/{pronostico["Temperatura m�nima"]}�C')
