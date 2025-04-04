"""
83. Modifica el código del ejercicio anterior para que el programa permita repetir x partidas (hasta 
que el usuario lo decida). Tienes que controlar una puntuación de cada partida de la siguiente 
manera, si la palabra la aciertas a la primera son 8 puntos, si la aciertas a la segunda 7 puntos y así 
sucesivamente.
Una vez el usuario desea finalizar el programa tiene que sumar todas tus puntuaciones obtenidas. 
Si el total supera la media de la puntuación posible de todas las partidas, se puede decir que la 
suerte le acompaña, de lo contrario mejor no Se dediques a los juegos de azar . PISTA.. ¿existe 
algún método que permita sumar el contenido de una lista?
"""

import random
puntos=8
a="casa,barco,gato,perro,madera,agua,puente,pantalón"
lista=[]
lista=a.split(",")
b=random.randint(1,8)
if b==1:
    d=lista[0]
elif b==2:
    d=lista[1]
elif b==3:
    d=lista[2]
elif b==4:
    d=lista[3]
elif b==5:
    d=lista[4]
elif b==6:
    d=lista[5]
elif b==7:
    d=lista[6]
elif b==8:
    d=lista[7]

f=0
g=1
while f<g:
    c=input("Intenta adivinar la palabra: ")
    if c!=d:
        print("No la acertaste")
        puntos=puntos-1
    elif c==d:
        print("La acertatse")
        f=1
        print(f"Tienes {puntos} puntos")