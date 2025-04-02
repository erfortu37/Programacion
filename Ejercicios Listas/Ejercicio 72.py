"""
72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y 
no deben almacenarse en la lista
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
                if letra=="à" or letra=="á":
                    letra="a"
                if letra=="é" or letra=="è":
                    letra="e"
                if letra=="ó" or letra=="ò":
                    letra="o"
                if letra=="í" or letra=="ì":
                    letra="i"
                if letra=="ú" or letra=="ù":
                    letra="u"
                lista.append(letra)
                norep=1
        elif preg=="n":
            var=1
            norep=1

lista2=[]
voc="á","é","í","ó","ú","à","è","ì","ò","ù"

for recorrer in (lista):
    if recorrer not in lista2:
        lista2.append(recorrer)

print(lista2)