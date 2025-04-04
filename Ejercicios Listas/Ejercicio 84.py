"""
84. A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las 
palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la 
palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra. 
"""

import random
f=0
g=1
lista1=['s','c','a','a']
lista2=['c','o','r','b','a']
lista3=['a','o','t','g']
lista4=['o','r','p','e','r']
lista5=['a','r','d','d','e','a','m']
lista6=['u','a','a','g']
lista7=['p','e','n','t','e','u']
lista8=['l','ó','n','n','a','t','a','p']
a=random.randint(1,8)
if a==1:
    print(lista1)
    b=input("Qué palabra es? ")
    while f<g:
        if b=="casa":
            print("Correcto")
            f=1
        else:
            print("Incorrecto")
elif a==2:
    print(lista2)
    b=input("Qué palabra es? ")
    while f<g:
        if b=="barco":
            print("Correcto")
            f=1
        else:
            print("Incorrecto")
elif a==3:
    print(lista3)
    b=input("Qué palabra es? ")
    while f<g:
        if b=="gato":
            print("Correcto")
            f=1
        else:
            print("Incorrecto")
elif a==4:
    print(lista4)
    b=input("Qué palabra es? ")
    while f<g:
        if b=="perro":
            print("Correcto")
            f=1
        else:
            print("Incorrecto")
elif a==5:
    print(lista5)
    b=input("Qué palabra es? ")
    while f<g:
        if b=="madera":
            print("Correcto")
            f=1
        else:
            print("Incorrecto")
elif a==6:
    print(lista6)
    b=input("Qué palabra es? ")
    while f<g:
        if b=="agua":
            print("Correcto")
            f=1
        else:
            print("Incorrecto")
elif a==7:
    print(lista7)
    b=input("Qué palabra es? ")
    while f<g:
        if b=="puente":
            print("Correcto")
            f=1
        else:
            print("Incorrecto")
elif a==8:
    print(lista8)
    b=input("Qué palabra es? ")
    while f<g:
        if b=="pantalón":
            print("Correcto")
            f=1
        else:
            print("Incorrecto")