# Ejercicio 20. A partir del ejercicio anterior, forzar que el usuario solo pueda
# introducir por teclados números entre 0 y 10.

var_1=int(input("Introduce un número entre el 0 y el 10:"))
var_2=int(input("Introduce otro número entre el 0 y el 10:"))
if var_1>0 and var_1<10:
    if var_2>0 and var_2<10:
        if var_1==var_2: print("ambos números son iguales:", var_1)
        elif var_1>var_2: print("el 1º número es mayor que el 2º:", var_1, var_2)
        else: print("el 1ª número es menor que el 2º:", var_1, var_2)
    else:print("Uno o los dos números están fuera de los límites establecidos")
else:print("Uno o los dos números están fuera de los límites establecidos")
