import webbrowser

# Ingresar la busqueda
query = input("Que quiere buscar?: ")
browser = "https://www.google.com/search?q="

buscar=browser+query

# Abrir Browser
webbrowser.open(buscar)

