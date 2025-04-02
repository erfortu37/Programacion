"""
63. Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número
de veces que se repite cada número.
"""

import random

cont=0
n1m=0
n2m=0
n3m=0
n4m=0
n5m=0
n6m=0
while cont<100:
    rndm=random.randint (1,6)
    
    if rndm==1:
        n1m=n1m+1
    elif rndm==2:
        n2m=n2m+1
    elif rndm==3:
        n3m=n3m+1
    elif rndm==4:
        n4m=n4m+1
    elif rndm==5:
        n5m=n5m+1
    elif rndm==6:
        n6m=n6m+1
    cont+=1

print(f"Uno: {n1m}")
print(f"Dos: {n2m}")
print(f"Tres: {n3m}")
print(f"Cuatro: {n4m}")
print(f"Cinco: {n5m}")
print(f"Seis: {n6m}")

print("programa finalizado")