"""
66. Repite el ejercicio 63. En lugar de ‘tirar’ 100 veces un dado, modifica el programa para ver cómo 
se comporta el dado en lanzamientos producidos durante aprox 3 segundos.
"""

import random
import time

tiempo=time.time()
tiempo_1=0
tiempo_cont=0
n1m=0
n2m=0
n3m=0
n4m=0
n5m=0
n6m=0
while tiempo_cont<3:
    tiempo_1=time.time()
    tiempo_cont=tiempo_1-tiempo
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

print(f"Uno: {n1m}")
print(f"Dos: {n2m}")
print(f"Tres: {n3m}")
print(f"Cuatro: {n4m}")
print(f"Cinco: {n5m}")
print(f"Seis: {n6m}")
print(f"El tiempo aproximado es {tiempo_cont}")

print("programa finalizado")