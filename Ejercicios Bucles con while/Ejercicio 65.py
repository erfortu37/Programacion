"""
65. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
-99. Por pantalla debe aparecer cuál de todos los números introducidos es el mayo y cuál el menor.
"""

cont=0
pars=0
impars=0
negnum=0
posnum=0
ceros=0
numay=0
numen=0
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
    if cont<numen and cont!=-99:
        numen=cont
    if cont>numay and cont!=(-99):
        numay=cont

sumtot=sumtot+99
    
print(f"El numero de pares es {pars}")
print(f"El numero de impares es {impars-1}")
print(f"El numero de positivos es {posnum}")
print(f"El numero de negativos es {negnum-1}")
print(f"El numero de ceros es {ceros}")
print(f"El total es {sumtot}")
print(f"El numero menor es {numen}")
print(f"El numero mayor es {numay}")