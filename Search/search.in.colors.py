# This script will take an input query string from the user, search Google, and print search results in different colors.
# shell : pip install googlesearch-python termcolor

from googlesearch import search
from termcolor import colored

# Take user input
query = input("Ingresar lo que se quiere buscar: ")

colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
color_index = 0

try:
   print(f"Resultados para: '{query}':\n")
   for result in search(query, num_results=10):
            print(colored(result, colors[color_index]))
            color_index = (color_index + 1) % len(colors)
except Exception as e:
       print(f"Error ocurrio durante la busqueda: {e}")


