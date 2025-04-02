# 58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while.

import random

num=random.randint(1, 5)
var=0

while var<3:
    intento=int(input("Intenta adivinar un numero entre el 1 y el 5: "))
    if intento==num:
        print("Numero acertado")
        var=5
    else:
        if intento>5 or intento<1:
            print("No has introducido nigun numero requerido")
        elif intento!=num:
            print("Numero no acertado")
    var+=1