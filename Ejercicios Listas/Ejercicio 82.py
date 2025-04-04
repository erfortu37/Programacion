"""
82. Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al 
azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine 
la palabra
"""

import random
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
    elif c==d:
        print("La acertatse")
        f=1