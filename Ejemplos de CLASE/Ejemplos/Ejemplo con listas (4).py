"""
Ejercicio de ejemplo con listas
"""

milista=input("Introduce una lista de numeros y letras separada por guiones: ")

lista=milista.split("-")

listnum=[]
letras=[]

print(lista)

for x in lista:
    if x.isnumeric():
        listnum.append(x)
    if x.isalpha():
        letras.append(x)
        
print(lista)
print(listnum)
print(letras)
lista3=[int(x) for x in listnum]
print(sum(lista3))