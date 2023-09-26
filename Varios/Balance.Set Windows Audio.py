from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume       # pip install pycaw
import math

# Get default audio device using PyCAW
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Get current volume of the left and right channels
currentVolumeLeft = volume.GetChannelVolumeLevel(0)
currentVolumeRight = volume.GetChannelVolumeLevel(1)

valorL=input("Ingresar valor de volumen (0 a 100) Left: {}\b\b".format(67))
if(len(valorL))==0:
 valorL=67                                                       # Valor por Default en Windows 
 
valorL=int(valorL)/100                                           # Los valores en la funcion son flotantes y entre 0.0 y 1.0. 

valorR=input("Ingresar valor de volumen (0 a 100) Right: {}\b\b".format(67))
if(len(valorR))==0:
 valorR=67                                                       # Valor por Default en Windows

valorR=int(valorR)/100                                           # Los valores en la funcion son flotantes y entre 0.0 y 1.0. 


volume.SetChannelVolumeLevelScalar(0,valorL,None)
volume.SetChannelVolumeLevelScalar(1,valorR,None)

#delta = abs(currentVolumeRight - currentVolumeLeft)
#mean = (currentVolumeLeft + currentVolumeRight) / 2
#print(currentVolumeLeft, currentVolumeRight, delta, mean, volume.GetVolumeRange(),volume.GetMasterVolumeLevel(),volume.GetMute())
