decimal = input("Ingrese un numero decimal:")

# Validar si el valor ingresado es un numero decimal
if decimal.isdecimal():
    decimal = int(decimal)
    hexa = hex(decimal)
    octal = oct(decimal)
    binario = bin(decimal)

    print("\nEl valor decimal", decimal, "es en:")
    print("Hexadecimal:", hexa)
    print("Octal      :", octal)
    print("Binario    :", binario)
else:
    print("El valor ingresado no es un numero decimal valido.")
