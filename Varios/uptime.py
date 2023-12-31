import os

if os.name == 'nt':                                              # Verifica que se este corriendo en Windows para poder importar la funcion ctypes
 import ctypes                                                   # Necesario para utilizar la funcion GetTickCount64()

else:
 with open('/proc/uptime', 'r') as f:                            # Procedimiento para linux
      uptime_seconds = str(f.readline().split(".")[0])           # Lee el valor que es un flotante pero corta la string cuando encuentra un .

      mins, seg = divmod(int(uptime_seconds), 60)                # Con el valor en segundos, ahora se tienen los minutos
      horas, mins = divmod(mins, 60)                             # Los cuales se los pasa a horas
      dias, horas = divmod(horas, 24)                            # y por ultimo en dias
      print(f"{dias} dias, {horas:02}:{mins:02}:{seg:02}")       # (format = x days, HH:MM:SS)

 exit()
                                                    
 
lib = ctypes.windll.kernel32                                     # Toma de las librerias del kernel donde esta GetTickCount64()
 
t = lib.GetTickCount64()                                         # Llama a la funcion GetTickCount64() 

#print(t) 

t = int(str(t)[:-3])                                             # El valor retornado esta en milisegundos por lo tanto se le quitan las ultimas cifras

#print(t)

mins, seg = divmod(t, 60)                                        # Con el valor en segundos, ahora se tienen los minutos
horas, mins = divmod(mins, 60)                                   # Los cuales se los pasa a horas
dias, horas = divmod(horas, 24)                                  # y por ultimo en dias
 


print(f"{dias} dias, {horas:02}:{mins:02}:{seg:02}")            # (format = x days, HH:MM:SS)