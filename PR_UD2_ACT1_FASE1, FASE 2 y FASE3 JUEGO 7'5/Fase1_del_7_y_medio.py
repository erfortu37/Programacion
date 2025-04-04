"""
Ejercicio del 7 y medio

FASE 1
"""

import random
var_while=0
var_while_2=1
v=0
variable_rep_part=0
var_rep_part=1
var_8__9=0
if_no_rep=0

print("Bienvenido al juego del 7 y medio")
while variable_rep_part<var_rep_part:
    if_no_rep=0
    v=0
    empzr_part=input("¿Estás listo para empezar la partida?(s/n): ")
    if empzr_part=="s":
        var_while=0
    elif empzr_part=="n":
        print("Veo que aún no estás preparado, vuelve más tarde.")
        var_while=1
        variable_rep_part=1
        if_no_rep=1        
    
    while var_while<var_while_2:
        carta=input("¿Quieres carta?(s/n): ")
        if carta=="s":
            num_randm=random.randint(1,12)
            if num_randm==8 or num_randm==9:
                var_8__9=random.randint(1,2)
                if var_8__9==1:
                    num_randm=random.randint(1,7)
                elif var_8__9==2:
                    num_randm=random.randint(10,12)
            print(f"Tu carta es: {num_randm}")
            if num_randm==10 or num_randm==11 or num_randm==12:
                num_randm=0.5
            v+=num_randm
            print(f"Acumulas en total: {v}")
            print("_________________________________")
            print(" ")
        elif carta=="n":
            var_while=1
        if v>7.5:
            print("Has perdido la partida!")
            var_while=1
        elif v==7.5:
            print("Enhorabuena, has ganado la partida")
            var_while=1
    if v>0:
        if v<7.1 and v>=5.9:
            print("Has sido un poco conservador")
        elif v<6:
            print("Quizás tendrías que arriesgar un poco ¿no?")
    
    while if_no_rep<1:
        rep_part=input("¿Quieres repetir la partida?(s/n): ")
        if rep_part=="s":
            variable_rep_part=0
        elif rep_part=="n":
            variable_rep_part=1
        if_no_rep=1