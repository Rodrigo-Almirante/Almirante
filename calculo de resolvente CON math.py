import math

def calcular_resolvente(a, b, c):
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return x1, x2
    elif discriminante == 0:
        x = -b / (2*a)
        return x
    else:
        return "No hay soluciones reales"

# Solicitar los valores de los coeficientes al usuario
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

# Calcular y mostrar la resolvente
resolvente = calcular_resolvente(a, b, c)
print("La resolvente de la ecuacion es:", resolvente)
