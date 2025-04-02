
"""
64. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
-99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas:

a) total de pares
b) total de impares
c) total de números positivos
d) total de números negativos
e) total de ceros
f) total de la suma de todos los números introducidos
"""

cont=0
pars=0
impars=0
negnum=0
posnum=0
ceros=0
sumtot=0

while cont !=(-99):
    cont=int(input("Introduce cualquier número (positivo, negativo y 0): "))
    
    if cont==0:
        ceros+=1
    if cont%2==0:
        pars+=1
    if cont%2==1:
        impars+=1
    if cont<0:
        negnum+=1
    if cont>0:
        posnum+=1
    sumtot=sumtot+cont

sumtot=sumtot+99
    
print(f"El numero de pares es {pars}")
print(f"El numero de impares es {impars-1}")
print(f"El numero de positivos es {posnum}")
print(f"El numero de negativos es {negnum-1}")
print(f"El numero de ceros es {ceros}")
print(f"El total es {sumtot}")