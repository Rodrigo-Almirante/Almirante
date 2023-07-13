
input_string = "3,1417"
value=input_string.split(",")[0]
print(value)

converted = int(input_string.split(",")[0],10)

print(converted)  # 3.14

Oficial = '276,890'
Blue    = '503,000'

numero1=int(Oficial.split(",")[0],10)
numero2=int(Blue.split(",")[0],10)

diferencia = numero2 - numero1
Brecha = (diferencia / numero1) * 100

print(" Oficial :$ ",numero1,"\n","Blue    :$ ",numero2,"\n\n","Brecha  :%",Brecha)
