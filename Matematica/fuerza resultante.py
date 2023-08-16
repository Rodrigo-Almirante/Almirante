# coding: cp1252                                                 # Se tiene que utilizar por los acentos
import math

def calcular_fuerza_resultante():
    # Pedir al usuario los valores de las fuerzas y el ángulo
    fuerza_1 = input("Ingrese el valor de la primera fuerza: ")
    fuerza_2 = input("Ingrese el valor de la segunda fuerza: ")
    angulo_1 = input("Ingrese el ángulo de dirección de la primera fuerza en grados: ")
    angulo_2 = input("Ingrese el ángulo de dirección de la segunda fuerza en grados: ")

    # Validar los valores ingresados
    try:
        fuerza_1 = float(fuerza_1)
        fuerza_2 = float(fuerza_2)
        angulo_1 = float(angulo_1)
        angulo_2 = float(angulo_2)
    except ValueError:
        print("Los valores ingresados no son válidos. Intente nuevamente.")
        return

    # Convertir los ángulos a radianes
    angulo_1_rad = angulo_1 * (3.14159 / 180)
    angulo_2_rad = angulo_2 * (3.14159 / 180)

    # Calcular las componentes x e y de cada fuerza
    fuerza_1_x = fuerza_1 * math.cos(angulo_1_rad)
    fuerza_1_y = fuerza_1 * math.sin(angulo_1_rad)
    fuerza_2_x = fuerza_2 * math.cos(angulo_2_rad)
    fuerza_2_y = fuerza_2 * math.sin(angulo_2_rad)

    # Calcular las componentes x e y de la fuerza resultante sumando las componentes de las fuerzas
    fuerza_resultante_x = fuerza_1_x + fuerza_2_x
    fuerza_resultante_y = fuerza_1_y + fuerza_2_y

    # Calcular el valor y dirección de la fuerza resultante
    fuerza_resultante = math.sqrt(fuerza_resultante_x**2 + fuerza_resultante_y**2)
    angulo_resultante_rad = math.atan2(fuerza_resultante_y, fuerza_resultante_x)
    angulo_resultante_grados = angulo_resultante_rad * (180 / 3.14159)

    # Imprimir el resultado
    print("El valor de la fuerza resultante es:", fuerza_resultante)
    print("El ángulo de dirección de la fuerza resultante es:", angulo_resultante_grados, "grados.")

# Llamar a la función principal
calcular_fuerza_resultante()
