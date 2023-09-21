from datetime import datetime

# Obtener la fecha actual
fecha_actual = datetime.now().date()
# Obtener la primera fecha ingresada por el usuario
fecha_1 = input("Ingrese la primera fecha (dd/mm/yyyy): {} \b\b\b\b\b\b\b\b\b\b\b".format(fecha_actual.strftime("%d/%m/%Y")))

# Verificar si se ingresó una fecha
if (len(fecha_1))==10:
    # Convertir la fecha ingresada a un objeto de fecha
    dia, mes, anio = map(int, fecha_1.split('/'))
    fecha_objeto_1 = datetime(anio, mes, dia).date()
else:
    fecha_objeto_1 = fecha_actual

# Obtener la segunda fecha ingresada por el usuario
fecha_2 = input("Ingrese la segunda fecha (dd/mm/yyyy): {} \b\b\b\b\b\b\b\b\b\b\b".format(fecha_actual.strftime("%d/%m/%Y")))

# Verificar si se ingresó una fecha
if (len(fecha_2))==10:
    # Convertir la fecha ingresada a un objeto de fecha
    dia, mes, anio = map(int, fecha_2.split('/'))
    fecha_objeto_2 = datetime(anio, mes, dia).date()
else:
    fecha_objeto_2 = fecha_actual


# Calcular la diferencia en días entre las dos fechas
diferencia = abs(fecha_objeto_2 - fecha_objeto_1)
cantidad_dias = diferencia.days

print("\nLa cantidad de días entre",fecha_objeto_1,"y",fecha_objeto_2,"es de:", cantidad_dias)

input("\nPersione enter para continuar...")