"""
80. Utilizando listas, crea un programa que te permita determinar si un número es decimal o no.
"""

lista=[]
numero=""

numero=input("Introduce un número: ")
lista=numero.split(".")

if len(lista)==2:
    if lista[0].isnumeric and lista[1].isnumeric:
        print("ES numero con decimal")
    else:
        print("No es un número con decimales")
else:
    print("No es un número con decimales")
    
print(lista)