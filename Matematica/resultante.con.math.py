# coding: cp1252                                                 # Se tiene que utilizar por los acentos

import math

def calcular_resultante():
    # Pedir al usuario los valores de los vectores
    vector_x = float(input("Ingrese el valor en x del vector: "))
    vector_y = float(input("Ingrese el valor en y del vector: "))
    
    # Validar los valores ingresados
    if math.isnan(vector_x) or math.isnan(vector_y):
        print("Los valores ingresados no son válidos. Intente nuevamente.")
        return
    
    # Calcular la magnitud del vector utilizando el teorema de Pitágoras
    magnitud = math.sqrt(vector_x**2 + vector_y**2)
    
    # Imprimir el resultado
    print("La magnitud del vector es:", magnitud)

# Llamar a la función principal
calcular_resultante()
