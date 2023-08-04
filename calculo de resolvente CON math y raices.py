import math

a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

D = b**2 - 4*a*c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print("Las raices son reales y diferentes.")
    print("x1 =", x1)
    print("x2 =", x2)
elif D == 0:
    x = -b / (2*a)
    print("La ecuacion tiene una raiz real doble.")
    print("x =", x)
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-D) / (2*a)
    print("Las raices son imaginarias.")
    print("x1 =", complex(real_part, imaginary_part))
    print("x2 =", complex(real_part, -imaginary_part))
