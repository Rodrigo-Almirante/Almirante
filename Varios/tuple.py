# Crear el tupla de dos dimensiones
tuple_2d = (('a', 1), ('b', 2), ('c', 3), ('d', 4))

# Obtener la cantidad de elementos de letras y de numeros
cantidad_letras = sum(isinstance(elemento[0], str) for elemento in tuple_2d)
cantidad_numeros = sum(isinstance(elemento[1], int) for elemento in tuple_2d)
print("La cantidad de elementos de letras es:", cantidad_letras)
print("La cantidad de elementos de numeros es:", cantidad_numeros)

# Contar la cantidad de elementos de letras y de numeros
cantidad_letras_count = sum(elemento[0].count('') for elemento in tuple_2d)
cantidad_numeros_count = sum(str(elemento[1]).count('') for elemento in tuple_2d)
print("La cantidad de elementos de letras (utilizando count) es:", cantidad_letras_count)
print("La cantidad de elementos de numeros (utilizando count) es:", cantidad_numeros_count)

# Imprimir el contenido de la tupla con dos bucles for
print("\n\bContenido del tuple:")
for i, (letra, numero) in enumerate(tuple_2d, start=0):
    if isinstance(letra, str):
        print(f"Elemento {i}: {letra} - letra")
    if isinstance(numero, int):
        print(f"Elemento {i}: {numero} - numero")

print("\n\bContenido del cuarto elemento:",tuple_2d[3][0]+":"+str(tuple_2d[3][1]))
