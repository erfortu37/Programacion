"""
Ejemplo de hacer listas
"""

total=0
milista=[]
milist2=[]
numero=int(input("Introduce un numero: "))

while numero!=0:
    milista.append(numero)
    numero=int(input("Introduce otro numero (0 para salir): "))
print(milista)

print(f"El nº maximo de la lista es {max(milista)}")
print(f"El nº minimo de la lista es {min(milista)}")

print(f"La suma total de la lista es {sum(milista)}")

milista2=[x*2 for x in milista]
print(milista2)