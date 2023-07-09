valor_octal = input("Ingrese un valor en octal: ")

try:
    decimal = int(str(valor_octal), 8)
    print("\nValor decimal     :", decimal)
    print("Valor hexadecimal :", hex(decimal))
    print("Valor binario     :", bin(decimal))
except ValueError:
    print("El valor ingresado no es valido en octal.")
