"""
70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez 
introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por 
pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el 
formato de entrada y salida tal y como se muestra en el testeo.
"""

lista1=[]

nº=int(input("Cuantas palabras quieres introducir: "))

for x in range (nº):
    palabra=input("Introduce una palabra: ")
    lista1.append(palabra)

print(f"lista1 contiene {lista1}")

lista1.reverse()
print(f"lista2 contiene {lista1}")