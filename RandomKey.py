import random
import keyboard
import msvcrt
from ctypes import windll
#Se colocan las teclas que se quiere que presionen solas
keys = ['w', 'a', 's', 'd', ' ']
count = 0
#Inicia el progrma apretando la tecla c
print("Presione c")
key = msvcrt.getwch()
if key == 'c':
    print("Starter")

#El programa evalua que se oprimio la tecla C para iniciar el ciclo
    while key == 'c':
        mh = random.choice(keys)
        keyboard.write(mh, delay=0.01)
        count = count + 1
        print(mh, count)
#El programa detecta si se presiono la tecla indicada para terminar el ciclo
        if keyboard.is_pressed('c'):
            key = None
            print("Stop")
            key = msvcrt.getwch()

