"""
59. Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que 
intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o 
menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe 
mostrarse por pantalla un mensaje y el número de intentos.
"""

import random
num=random.randint(0, 1000)
var=0
intentos=0
bucle=1

while var<bucle:
    a=int(input("Introduce un valor comprendido entre 0 y 1000: "))
    
    if a<num:
        print("El numero que has introducido es menor")
    elif a>num:
        print("El numero que has introducido es mayor")
    intentos+=1
    if a==num:
        print(f"Acertaste, has realizado {intentos} intentos")
        var=1