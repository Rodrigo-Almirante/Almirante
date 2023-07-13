def hanoi(n, origen, destino, auxiliar):
    if n > 0:
        # Movemos n-1 discos de origen a auxiliar
        hanoi(n-1, origen, auxiliar, destino)
        # Movemos el disco n de origen a destino
        print("Mover disco", n, "de", origen, "a", destino)
        # Movemos n-1 discos de auxiliar a destino
        hanoi(n-1, auxiliar, destino, origen)

# Pedir al usuario la cantidad de discos
n = int(input("Ingrese la cantidad de discos: "))

# Resolver las Torres de Hanoi
hanoi(n, 'A', 'C', 'B')
