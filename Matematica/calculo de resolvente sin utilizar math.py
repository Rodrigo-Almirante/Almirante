a = float(input("Ingresa el coeficiente a: "))
b = float(input("Ingresa el coeficiente b: "))
c = float(input("Ingresa el coeficiente c: "))

# Calcular el discriminante
discriminante = b**2 - 4*a*c

# Calcular la resolvente
if discriminante > 0:
    x1 = (-b + discriminante**0.5) / (2*a)
    x2 = (-b - discriminante**0.5) / (2*a)
    print("Las raices de la ecuacion son: x1=", x1, "y x2=", x2)
elif discriminante == 0:
    x = -b / (2*a)
    print("La raiz de la ecuacion es:", x)
else:
    parte_real = -b / (2*a)
    parte_imaginaria = (-discriminante)**0.5 / (2*a)
    print("Las raices de la ecuacion son complejas:")
    print("x1 =", parte_real, "+", parte_imaginaria, "i")
    print("x2 =", parte_real, "-", parte_imaginaria, "i")
