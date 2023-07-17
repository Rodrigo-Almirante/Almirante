# coding: cp1252                                                 # Se tiene que utilizar por los acentos, en especial en la URL si es que los tiene

# importing library
import requests                                                  # pip requests
from bs4 import BeautifulSoup                                    # pip BeautifulSoup
 
# Nombre de la ciudad
ciudad = "Santa Fe de la Vera Cruz"
 
# Crear a la url correspondiente
url = "https://www.google.com/search?q="+"weather"+ciudad
html = requests.get(url).content
 
# Datos en forma pura
soup = BeautifulSoup(html, 'html.parser')
#print(soup)                                                     # Imprimir que lee en formato HTML
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text  # Busca la clase BNeawe iBp4i AP7Wnd
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
 
# Formato de los datos
data = str.split('\n')
hora = data[0]
clima = data[1]
 
# Leer todos los div tag
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
strd = listdiv[5].text
 
# Datos necesarios
pos = strd.find('Humedad')
otros_datos = strd[pos:]
 
# printing all data
print("\nCiudad      :",ciudad)
print("Fecha       :",hora.capitalize())
print("Temperatura :",temp)
print("Clima       :", clima)
print("Info Extra  :",otros_datos)