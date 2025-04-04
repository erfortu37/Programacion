"""
Ejemplo lista
"""

texto=input("Introduce una frase frasonga: ")

milista=[]
milista= texto.split()

print(milista)

palabra=input("Introduce la palabra a buscar: ")

print("El nº de palabras es:", milista.count(palabra))

frase1="-".join(milista)

print(frase1)