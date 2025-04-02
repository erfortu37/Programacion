"""
78. A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea 
eliminar de la lista, siendo únicamente los números los valores permitidos para suprimi
"""

lista1=['a','b','D','x','r','X','3','h','w','2','i']
f=0
g=1
while f<g:
    a=input("Introduce el caracter que quieres eliminar: ")
    if a=="a":
        lista1.pop(0)
        print(lista1)
    elif a=="b":
        lista1.pop(1)
        print(lista1)
    elif a=="D":
        lista1.pop(2)
        print(lista1)
    elif a=="x":
        lista1.pop(3)
        print(lista1)
    elif a=="r":
        lista1.pop(4)
        print(lista1)
    elif a=="X":
        lista1.pop(5)
        print(lista1)
    elif a=="3":
        lista1.pop(6)
        print(lista1)
    elif a=="h":
        lista1.pop(7)
        print(lista1)
    elif a=="w":
        lista1.pop(8)
        print(lista1)
    elif a=="2":
        lista1.pop(9)
        print(lista1)
    elif a=="i":
        lista1.pop(10)
        print(lista1)
    elif a not in lista1:
        print("El valor introducido no está en la lista")
    b=input("Desea introducir otro caracter(s/n): ")
    if b=="n":
        f=1