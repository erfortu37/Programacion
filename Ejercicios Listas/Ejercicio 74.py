"""
74. A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de 
entre las 2 listas.
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
        
for cont in lista2:
    if cont not in lista1:
        lista4.append(cont)
    
    
print (f"Estan repetidas: {lista3}")
print (f"No estan repetidas: {lista4}")