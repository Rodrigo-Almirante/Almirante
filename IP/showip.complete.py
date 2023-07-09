# Muestra la IP externa utilizando la pagina showmyip.com

import requests

url = 'https://www.showmyip.com/'

response = requests.get(url)

if response.status_code == 200:

    start = response.text.find('Your IPv4') + len('Your IPv4</td><td><b>')
    end = response.text.find('</b>', start)
    current_ip = response.text[start:end]
    print(f"\nLa direccion IP es : \x1b[2;30;47m{current_ip}\x1b[0m")

    start = response.text.find('<td>Country') + len('<td>Country</td><td>')
    end = response.text.find('</td>', start)
    country = response.text[start:end]
    print(f"Pais               : {country}")

    start = response.text.find('<td>City') + len('<td>City</td><td>')
    end = response.text.find('</td>', start)
    city = response.text[start:end]
    print(f"Ciudad             : {city}")

    start = response.text.find('<td>ZIP') + len('<td>ZIP</td><td>')
    end = response.text.find('</td>', start)
    zipcode = response.text[start:end]
    print(f"Codigo Postal      : {zipcode}")

    start = response.text.find('<td>Internet Service Provider (ISP)') + len('<td>Internet Service Provider (ISP)</td><td>')
    end = response.text.find('</td>', start)
    isp = response.text[start:end]
    print(f"ISP                : {isp}")


    start = response.text.find('<td>Organization') + len('<td>Organization</td><td>')
    end = response.text.find('</td>', start)
    organization = response.text[start:end]
    print(f"Organizacion       : {organization}")


    start = response.text.find('<td>User agent') + len('<td>User agent</td><td>')
    end = response.text.find('</td>', start)
    useragent = response.text[start:end]
    print(f"User Agent         : {useragent}")

else:
    print("No se pudo conectar al website.")
