"""
71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en 
esta lista no deben almacenarse las letras que se han introducido repetidas.
"""

lista=[]
var=0
var_while=1
norep=0
norep1=1

while var<var_while:
    letr_inic=input("Introduce una letra: ")
    if letr_inic.isalpha():
        lista.append(letr_inic)
        var=1
    else:
        var=0

var=0
    
while var<var_while:
    preg=input("¿Quieres introducir otra letra?(s/n): ")
    norep=0
    while norep<norep1:
        if preg=="s":
            letra=input("Introduce una letra: ")
            if letra.isalpha()==True:
                lista.append(letra)
                norep=1
        elif preg=="n":
            var=1
            norep=1

lista2=[]

for recorrer in (lista):
    if recorrer not in lista2:
        lista2.append(recorrer)

print(lista2)