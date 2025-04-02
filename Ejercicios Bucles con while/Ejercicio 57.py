# 57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5.
# El programa debe controlar si el usuario introduce un número no comprendido 
# entre 1 y 5.

import random

num=random.randint(1, 5)

intento=int(input("Intenta adivinar un numero entre el 1 y el 5: "))

if intento==num:
    print("Numero acertado")
else:
    if intento>5 or intento<1:
        print("No has introducido nigun numero requerido")
    elif intento!=num:
        print("Numero no acertado")
    