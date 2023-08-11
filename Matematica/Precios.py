
numero1 = float(input("\nIngrese el valor Actual  : $"))
numero2 = float(input("Ingrese el valor Anterior: $"))

# Verificar que el primero sea mayor que el segundo
while numero1 <= numero2:
    print("El valor ANTERIOR debe ser menor al Actual (Argentina reality). Por favor, ingrese un numero valido.")
    numero2 = float(input("Ingrese ANTERIOR nuevamente: "))

# Calcular el porcentaje
diferencia = numero1 - numero2
porcentaje = (diferencia / numero2) * 100

# Mostrar el resultado
print("\nEl porcentaje que aumento entre $"+str(int(numero1)), "y $"+str(int(numero2)), "es del %"+str(porcentaje))

input("\nPersione enter para continuar...")
