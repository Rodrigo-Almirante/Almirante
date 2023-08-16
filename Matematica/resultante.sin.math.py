# coding: cp1252                                                 # Se tiene que utilizar por los acentos

def calcular_resultante():
    # Pedir al usuario los valores de los vectores
    vector_x = input("Ingrese el valor en x del vector: ")
    vector_y = input("Ingrese el valor en y del vector: ")
    
    # Validar los valores ingresados
    try:
        vector_x = float(vector_x)
        vector_y = float(vector_y)
    except ValueError:
        print("Los valores ingresados no son válidos. Intente nuevamente.")
        return
    
    # Calcular la magnitud del vector utilizando el teorema de Pitágoras
    magnitud = (vector_x ** 2 + vector_y ** 2) ** 0.5
    
    # Imprimir el resultado
    print("La magnitud del vector es:", magnitud)

# Llamar a la función principal
calcular_resultante()
