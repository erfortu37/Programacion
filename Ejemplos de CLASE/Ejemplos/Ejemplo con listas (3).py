"""
Ejemplo con listas
"""

numeros=input("introduce numeros separados por espacios: ")

listanumeros=numeros.split()

print(listanumeros)

# lista2=[int(x) for x in listanumeros]

lista2=set(listanumeros)

print(lista2)