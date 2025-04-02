"""
73. Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están 
repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se 
repiten y cuales no
"""

lista1=['casa','mesa','sal','sol','agua']
lista2=['casa','luz','tres','tren','sol','pan']
lista3=[]
lista4=[]

print(f"La primera lista es esta {lista1}")
print(f"La segunda lista es {lista2}")

for recorrer in lista1:
    if recorrer not in lista2:
        lista4.append(recorrer)
    else:
        lista3.append(recorrer)
    
    
print (f"Estan repetidas: {lista3}")
print (f"No estan repetidas: {lista4}")