import string
valor = input("Ingrese un valor en hexadecimal: ")

if all(c in string.hexdigits for c in valor):
    decimal = int(valor, 16)
    octal = oct(decimal)
    binario = bin(decimal)
    print("\nValor decimal : ", decimal)
    print("Valor octal   : ", octal)
    print("Valor binario : ", binario)
else:
    print("\nEl valor ingresado no es un valor hexadecimal valido.")
