
porcentaje = input("\nIngresar el porcentaje mensual % : 7\b")
if not porcentaje:
  porcentaje = "7"

periodo = input("\nIngresar el Periodo en meses     : 12\b\b")
if not periodo:
  periodo = "12"

valor = 1 + float(porcentaje)/100
valor = ((valor**int(periodo))-1)*100                               # ((1 + Porcentaje Mensual) ^ Periodo - 1) * 100

print("\nCon una inflacion mensual de %"+porcentaje,"se tiene una inflacion en",periodo,"meses de %"+str(valor))
