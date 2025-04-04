"""
Fase 3 del 7 y medio
"""
# Aquí importo la biblioteca "random" para luego poder utilizar los métodos para generar
# números de forma aleatoria para realizar este juego.
import random
# Las siguiemtes 2 variables son unas variables de control para el primer while.
var_while=0
var_while_2=1
# Aquí nombro la variable "v" como el total acumulado del jugador.
v=0
# Aquí nombro la variable "v_2" como el total acumulado de la banca
v_2=0
# Esta variable es muy importante. Esta variable sirve para controlar que no haya
# ninguna carta con el valor de 8 o de 9.
var_8__9=0
# Las siguientes dos variables son unas variables que sirven para controlar el while del
# turno de la banca.
var_int_art=0
while_int_art=1
# Esta variable sirve simplemente para empezar el turno de la banca.
empezar_CPU=0

# Aquí introduzco el juego.
print("Bienvenido al juego del 7 y medio")
# En esta línea, pido un "alias"/nombre para que luego el programa mismo vaya
# preguntándole con ese alias.
alias=input("Ponte un nombre (alias): ")
# Inicialmente creo una variable "empzr_part" para saber si el jugador/alias quiere
# empezar. Esta variable se iguala a un input() para que el alias decida si poner
# "s", de sí, o "n", de no.
empzr_part=input(f"{alias}, ¿estás listo para empezar la partida?(s/n): ")
# Si el jugador está listo para empezar la partida, o sea que "empzr_part" es igual
# a "s", la variable control para el primer while no varía.
if empzr_part=="s":
    var_while=0
# En cambio, si la variable "empzr_part" es igual a "n", se printea un mensaje en
# el que el programa dice que el jugador aún no está listo y que vuelva cuando lo
# esté. Tambien, la primera variable control para iniciar la partida con el primer
# while, se iguala a 1 para que el while no se inicie. De otra forma, la variable
# que controla si la banca juega tambien se modifica igualándola a 1 para que no
# empieze, para que si el alias no juega, la banca tampoco.
elif empzr_part=="n":
    print(f"{alias} veo que aún no estás preparado, vuelve más tarde.")
    var_while=1
    empezar_CPU=1
        

# Si el jugador inicia la partida, empieza el bucle con while que irá pidiendo cartas
# hasta que el jugador diga que no, gane o pierda.    
while var_while<var_while_2:
# Aquí el programa pregunta al alias si quiere carta.
    carta=input(f"{alias}, ¿Quieres carta?(s/n): ")
# Si dice que sí que quiere carta, se iguala la variable "num_randm" a un número aleatorio
# de la biblioteca random, el número es del 1 al 12.
    if carta=="s":
        num_randm=random.randint(1,12)
# Si el número es un 8 o un 9, como el juego no los acepta, genera un número aleatorio
# entre el 1 y el 2 que se igualará al variable "var_8__9" para que vuelva a poner otro
# número.
        if num_randm==8 or num_randm==9:
            var_8__9=random.randint(1,2)
# Si la variable es 1, pongo que la variable que decide el número que se iguale a 
# un número aleatorio entre el 1 y el 7.
            if var_8__9==1:
                num_randm=random.randint(1,7)
# En cambio, si la variable es 2, se hará exactamente lo mismo que antes, pero en la
# variable "num_random" se generará un número aleatorio entre el 10 y el 12.
            elif var_8__9==2:
                num_randm=random.randint(10,12)
# Ahora printeo el nombre/el alias del jugador y le digo la carta que ha sacado con la
# "f" y las llaves en las comillas.
        print(f"{alias} tu carta es: {num_randm}")
# Como el 10, 11 y 12 en este juego no valen sus respectivos valores, si no que valen
# 0.5, pongo un "if" de que si salen estos números, que la variable valga 0.5.
        if num_randm==10 or num_randm==11 or num_randm==12:
            num_randm=0.5
# Ahora finalmente hago una variable: "v", para que sea todo lo acumulado, haciendo
# que "v" se igual a "v"+la carta correspondiente y no las
# cartas sueltas. Luego printeo una barra y unos espacios para que den más espacio 
# visual y que no se vea muy cargado, igual que el input.
        v+=num_randm
        print(f"{alias}, acumulas en total: {v}")
        print("_________________________________")
        print(" ")
        input()
# Si el usuario o el alias dice que no: "n", pues la variable para controlar el while se
# igualará a 1 para que no continue. Tambien se printea el total que tiene acumulado.
    elif carta=="n":
        var_while=1
        print(f"{alias}, acumulas en total: {v}")
# Si despues de pedir carta el usuario se ha pasado de 7 y medio, que la variable
# controladora del while sea 1 y que printee al usuario que se ha pasado.
    if v>7.5:
        print(f"{alias} te has pasado!")
        var_while=1
# Si en vez de haberse pasado, se ha quedado justo con 7 y medio, que tambien se 
# cancele el while y que le printee al alias que ha consegudio el máximo.
    elif v==7.5:
        print(f"Que suerte {alias}, has conseguido la puntuación máxima!")
        var_while=1
    
# Aquí pongo que si la variable para empezar es 0, eso quiere decir que el usuario ha 
# jugado la partida, que empieze la máquina. Primero printeo esspacios ylíneas para 
# que visualmente no se vea cargado. Después explico lo que hará la banca y pongo un input
# para que el jugador lo lea. Luego pregunta a la banca si quiere carta, obviamente
# dirá que sí y se realizará el mismo programa que cuando el jugador pedía una carta.
# Lo único que cambia de todo esto es el valor acumulado, que en vez de ser "v", es
# "v_2".
if empezar_CPU==0:
    print("")
    print("_________________________________")
    print("")
    print("Ahora es turno de la BANCA, jugará como si fuera otro jugador cualquiera")
    input()
    print("¿Quieres carta?(s/n): s")
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
    v_2+=num_randm
    print(f"Acumulas en total: {v_2}")
    print("_________________________________")
    print(" ")

# Después de pedir la primera carta, genero un while, con las variables control
# pero para la banca.
    while var_int_art<while_int_art:
# Aquí primero pongo un "if" para comprobar que no se haya pasado de 7 y medio
        if v_2!=7.5:
# En estas líneas de código dentro de el while, son todas las posibles combinaciones
# dentro de lo que pueda salir para que la banca gane.
# Aquí compruebo que si la banca tiene acumulado menos de 4 o que tenga 4, que pida carta.
                        if v_2<4 or v_2==4:
                            input()
                            print("Quieres carta?(s/n): s")
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
                            v_2+=num_randm
                            print(f"Acumulas en total: {v_2}")
                            print("_________________________________")
                            print(" ")
# Aquí compruebo que si la banca se pasa del 7 y medio, que no pueda pedir más cartas
                        elif v_2>7.5:
                            var_int_art=1
                            print("La BANCA se ha pasado")
# Aquí compruebo que si la banca es igual al jugador pero que sea mayor que 5 o igual
# que se plante y que empaten.
                        elif v_2==v and v_2>5 and v_2==5:
                            input()
                            print("Quires carta?(s/n): n")
                            var_int_art=1
# Si el jugador se ha pasado de 7 y medio y la banca si tiene más de 4, que se plante.
                        elif v_2>4 and v>7.5:
                            input()
                            print("Quires carta?(s/n): n")
                            var_int_art=1
# Si la banca es mayor que 4 pero si el jugador tiene más acumulado, que siga pidiendo.
                        elif v_2>4 and v>v_2:
                            input()
                            print("Quieres carta?(s/n): s")
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
                            v_2+=num_randm
                            print(f"Acumulas en total: {v_2}")
                            print("_________________________________")
                            print(" ")
# Si la banca es mayor de 4 y el jugador se ha pasado o tiene menor número, que se plante.
                        elif v_2>4 and v<v_2 or v>7.5 or v==5:
                            input()
                            print("Quires carta?(s/n): n")
                            var_int_art=1
# Si la banca es mayor a 5 y el jugador es igual a 7.5, que se plante para no pasarse.
                        elif v_2>5 and v==7.5:
                            input()
                            print("Quires carta?(s/n): n")
                            var_int_art=1
# Si la banca es mayor a 6.5, es decir "7", que se plante ya que es una buena puntuación.
                        elif v_2>6.5:
                            input()
                            print("Quires carta?(s/n): n")
                            var_int_art=1
# En el caso de que la banca tenga 7 y medio, que deje el bucle while y que printee
# el mensaje de que la banca tiene la puntuación máxima.
        else:
            print("La BANCA ha consegudo la puntuación máxima")
            var_int_art=1
            
# Aquí printeo, poniendo mensajes con todos los finales posibles, con la banca perdiendo
# o pasándose, con el jugador ganando o pasándose, empatando o incluso ajustando a 
# la puntuación máxima.
    if v<v_2 and v_2<7.5:
        print("¡¡¡HAS PERDIDO CONTRA LA BANCA!!!")
    elif v==v_2:
        print("Has empatado la partida contra la BANCA")
    elif v>v_2 and v<7.5:
        print("ENHORABUENA HAS GANADO A LA BANCA")
    elif v>7.5 and v_2<7.5:
        print("¡¡¡HAS PERDIDO CONTRA LA BANCA!!!")
    elif v_2>7.5 and v<7.5:
        print("ENHORABUENA HAS GANADO A LA BANCA")
    elif v_2>7.5 and v>7.5:
        print("¡¡¡HABEIS PERDIDO LOS DOS!!!")
    elif v_2==7.5 and v>7.5 or v<7.5:
        print("¡¡¡HAS PERDIDO CONTRA LA BANCA!!!")
    