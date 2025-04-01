# 39. Programa que pida n números y que, tras introducir el último número, debe aparecer por 
# pantalla el número total de positivos, negativos y número de 0.

a=int(input("¿Cuántos numeros quieres introducir?"))
ceros=0
pos=0
neg=0

for recorrer in range(a):
    num=int(input("Introduce un numero: "))
    if num==0:
        ceros=ceros+1
    elif num>0:
        pos=pos+1
    elif num<0:
        neg=neg+1

print("Numeros positivos: ", pos)
print("Numeros negativos: ", neg)
print("Ceros: ", ceros)