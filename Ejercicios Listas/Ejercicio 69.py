"""
69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se 
irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números 
ordenados de menor a mayor.
"""

lista=[]

nº=int(input("Cuantos numeros quieres introducir: "))

for x in range (nº):
    num=int(input("Introudce un numero: "))
    lista.append(num)

lista.sort()
print(lista)