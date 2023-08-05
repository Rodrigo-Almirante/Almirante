# coding: cp1252

# Función para calcular el determinante de una matriz
def calcular_determinante(matriz):
    n = len(matriz)
    det = 0
    
    # Caso base: si la matriz es de 1x1, el determinante es el elemento único de la matriz
    if n == 1:
        return matriz[0][0]
    
    # Si la matriz es de tamaño 2x2, utiliza la fórmula directamente
    if n == 2:
        det = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    else:
        # Si la matriz es de tamaño mayor a 2x2,
        # utiliza la expansión por cofactores para calcular el determinante
        for c in range(n):
            submatriz = [[0] * (n-1) for _ in range(n-1)]
            for i in range(1, n):
                submatriz[i-1] = matriz[i][0:c] + matriz[i][c+1:]
            det += (-1)**c * matriz[0][c] * calcular_determinante(submatriz)
    
    return det


# Ingreso de la matriz
n = int(input("Ingrese el tamaño de la matriz cuadrada: "))
matriz = []
print("Ingrese los elementos de la matriz fila por fila SEPARADOS por un espacio:")
for _ in range(n):
    fila = list(map(float, input().split()))
    matriz.append(fila)

# Calcular el determinante
determinante = calcular_determinante(matriz)

# Imprimir el resultado
print("El determinante de la matriz es:", determinante)
