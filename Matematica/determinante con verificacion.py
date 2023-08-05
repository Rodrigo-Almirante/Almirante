# coding: cp1252


def calcular_determinante(matriz):
    # Verificar que la matriz sea cuadrada
    filas = len(matriz)
    columnas = len(matriz[0])
    if filas != columnas:
        return "La matriz no es cuadrada"

    # Definir el caso base para matrices de 1x1
    if filas == 1:
        return matriz[0][0]

    # Calcular el determinante
    determinante = 0
    for columna in range(columnas):
        submatriz = []
        for fila in range(1, filas):
            fila_actual = matriz[fila][:columna] + matriz[fila][columna+1:]
            submatriz.append(fila_actual)
        signo = (-1)**columna
        determinante += signo * matriz[0][columna] * calcular_determinante(submatriz)

    return determinante

# Ingresar el tamaño de la matriz
filas = int(input("Ingresa el número de filas de la matriz: "))
columnas = int(input("Ingresa el número de columnas de la matriz: "))

# Verificar que la matriz sea cuadrada
if filas != columnas:
    print("La matriz debe ser cuadrada")
else:
    # Ingresar los valores de la matriz
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)

    # Calcular el determinante
    determinante = calcular_determinante(matriz)

    # Mostrar el resultado
    print("El determinante de la matriz es:", determinante)
    exit()

def calcular_determinante(matriz):
    # Verificar que la matriz sea cuadrada
    filas = len(matriz)
    columnas = len(matriz[0])
    if filas != columnas:
        return "La matriz no es cuadrada"

    # Definir el caso base para matrices de 1x1
    if filas == 1:
        return matriz[0][0]

    # Calcular el determinante
    determinante = 0
    filas_restantes = filas - 1
    for columna in range(columnas):
        submatriz = []
        for fila in range(1, filas):
            fila_actual = []
            for j in range(columnas):
                if j != columna:
                    fila_actual.append(matriz[fila][j])
            submatriz.append(fila_actual)
        signo = (-1)**columna
        determinante += signo * matriz[0][columna] * calcular_determinante(submatriz)

    return determinante

# Ingresar el tamaño de la matriz
filas = int(input("Ingresa el número de filas de la matriz: "))
columnas = int(input("Ingresa el número de columnas de la matriz: "))

# Verificar que la matriz sea cuadrada
if filas != columnas:
    print("La matriz debe ser cuadrada")
else:
    # Ingresar los valores de la matriz
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)

    # Calcular el determinante
    determinante = calcular_determinante(matriz)

    # Mostrar el resultado
    print("El determinante de la matriz es:", determinante)
