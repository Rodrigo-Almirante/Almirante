# Pedir al usuario que ingrese dos numeros

numero1 = float(input("\nIngrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))

# Verificar que el primero sea mayor que el segundo
while numero1 <= numero2:
    print("El segundo numero debe ser menor que el primero. Por favor, ingrese un numero valido.")
    numero2 = float(input("Ingrese el segundo numero nuevamente: "))

# Calcular el porcentaje
diferencia = numero1 - numero2
porcentaje = (diferencia / numero2) * 100

# Mostrar el resultado
print("\nEl porcentaje entre", numero1, "y", numero2, "es: %",porcentaje)

input("\nPersione enter para continuar...")
