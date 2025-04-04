# Ejercicio2.py (SUMATIVA)

recorrer=0
pos=0
neg=0

for recorrer in range (6):
    num=int(input(print("Introduce un número positivo o negativo:")))
    recorrer=recorrer+num
    if recorrer<0:
        neg=neg+num
    if recorrer>0:
        pos=pos+num
    recorrer=0

print("Suma de numeros positivos: 3")
print("Suma de numeros negativos:-3")