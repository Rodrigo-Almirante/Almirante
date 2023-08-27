tuple_dimensiones = (('a', 'b', 'c', 'd'), (1, 2, 3, 4), ('x', 'y', 'z'))

# Contar la cantidad de elementos de letras y numeros
cantidad_letras = sum(isinstance(elemento, str) for dimension in tuple_dimensiones for elemento in dimension)
cantidad_numeros = sum(isinstance(elemento, int) for dimension in tuple_dimensiones for elemento in dimension)

# Imprimir el contenido de la tuple
for dimension in tuple_dimensiones:
    for posicion, elemento in enumerate(dimension):
        if isinstance(elemento, str):
            print(f"{elemento} en la posicion {posicion} es una letra")
        elif isinstance(elemento, int):
            print(f"{elemento} en la posicion {posicion} es un numero")
        if posicion==3:
           print("\b")

# Imprimir el contenido del ultimo elemento del tuple
ultimo_elemento = tuple_dimensiones[2]
print(f"\n\bEl contenido del ultimo elemento del tuple es: {ultimo_elemento}")