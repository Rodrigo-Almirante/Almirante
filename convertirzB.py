valor_binario = input("Ingrese un valor en binario: ")

try:
    decimal = int(str(valor_binario), 2)
    print("\nValor decimal     :", decimal)
    print("Valor hexadecimal :", hex(decimal))
    print("Valor octal       :", oct(decimal))
except ValueError:
    print("El valor ingresado no es valido en binario.")
