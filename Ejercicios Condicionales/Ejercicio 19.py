# Ejercicio 19. Programa que introduzca dos números y devuelva cuál de los dos es
# mayor, menor o son iguales.

var_1=int(input("Introduce un número:"))
var_2=int(input("Introduce otro número:"))

if var_1==var_2: print("ambos números son iguales:", var_1)
elif var_1>var_2: print("el 1º número es mayor que el 2º:", var_1, var_2)
else: print("el 1º número es menor que el 2º:", var_1, var_2)
