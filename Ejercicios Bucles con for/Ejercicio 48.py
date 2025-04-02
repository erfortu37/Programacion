"""
48. Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de 
esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuario
tenga x oportunidades para ver si letra introducida está en esa palabra.
"""

a=input("Introduce una palabra secreta: ")

for x in range(len(a)):
    b=input("Introduce una letra: ")
    if b in a:
        print("La letra exsiste")
    else:
        print("La letra no exsiste")