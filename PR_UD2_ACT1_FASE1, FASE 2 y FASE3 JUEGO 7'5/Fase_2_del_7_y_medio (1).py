"""
Ejercicio 7 y medio

Fase 2
"""

import random
var_while=0
var_while_2=1
v=0
variable_rep_part=0
var_rep_part=1
var_8__9=0
if_no_rep=0
puntos=100

print("Bienvenido al juego del 7 y medio")
print("")
print("Empiezas con un contador de 100 puntos, si te quedas a 0, pierdes y ya no puedes seguir jugando")
print("Los puntos se sumarán según con cuantos puntos te plantes o si ganas o pierdes")
while variable_rep_part<var_rep_part:
    if_no_rep=0
    v=0
    print("_________________________________")
    print("")
    empzr_part=input("¿Estás listo para empezar la partida?(s/n): ")
    if empzr_part=="s":
        var_while=0
    elif empzr_part=="n":
        print("Veo que aún no estás preparado, vuelve más tarde.")
        var_while=1
        variable_rep_part=1
        if_no_rep=1
    
    variable_rep_part=0
    
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
            print("")
            print("Has perdido 10 puntos")
            var_while=1
            puntos=puntos-10
        elif v==7.5:
            print("Enhorabuena, has ganado la partida")
            print("")
            print("Has ganado 10 puntos")
            var_while=1
            puntos=puntos+10    
    if v>0:
        if v<7.1 and v>=5.9:
            print("Has sido un poco conservador")
            print("")
            print("Has ganado 5 puntos")
            puntos=puntos+5
        elif v<6:
            print("Quizás tendrías que arriesgar un poco ¿no?")
            print("")
            print("Has perdido 10 puntos")
            puntos=puntos-5
        
            
    print("")
    print(f"Ahora tienes ({puntos}) puntos")
    
    if puntos>0:
        while if_no_rep<1:
            rep_part=input("¿Quieres repetir la partida?(s/n): ")
            if rep_part=="s":
                variable_rep_part=0
            elif rep_part=="n":
                print("Bueno, pues hasta otra")
                variable_rep_part=1
            if_no_rep=1
            
    else:
        variable_rep_part=1
        print(f"Te has quedado sin puntos ({puntos}) ; ya no puedes seguir jugando")