#  in shell : pip install googlesearch-python

from googlesearch import search

# Take user input
query = input("Ingresar lo que se quiere buscar: ")

# Buscar
try:
    print("\nResultados:")
    for j in search(query, num_results=10):
        print(j)
except Exception as e:
    print(f"Error durante la busqueda: {e}")


