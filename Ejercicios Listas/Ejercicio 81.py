"""
81. A partir de una lista definida, busca el método apropiado para que se visualice un valor de la 
lista al azar.
"""

import random
a="casa,barco,gato,perro,madera,agua,puente,pantalón"
lista=[]
lista=a.split(",")
b=random.randint(1,8)
if b==1:
    print(lista[0])
elif b==2:
    print(lista[1])
elif b==3:
    print(lista[2])
elif b==4:
    print(lista[3])
elif b==5:
    print(lista[4])
elif b==6:
    print(lista[5])
elif b==7:
    print(lista[6])
elif b==8:
    print(lista[7])