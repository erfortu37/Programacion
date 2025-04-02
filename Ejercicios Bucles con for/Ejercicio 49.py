"""
49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado te 
indique en qué posición de la palabra se encuentra la letra.
"""

a=input("Introduce una palabra secreta: ")

for x in range(len(a)):
    b=input("Introduce una letra: ")
    if b in a:
        print("La letra exsiste")
        print(f"La letra se uncuentra en la posición {x}")
    else:
        print("La letra no exsiste")