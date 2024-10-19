# Ejercicio 7. programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes forzar que el resultado de la división tenga 2 decimales?

operador_1=int(input("Dime el operador 1:"))
operador_2=int(input("Dime el operador 2:"))

División_round = round(operador_1/operador_2, 2)

print("La suma de operador1 y operador2 es:", operador_1+operador_2)
print("La resta de operador1 y operador2 es:", operador_1-operador_2)
print("La multiplicación de operador1 y operador2 es:", operador_1*operador_2)
print("La división de operador1 y operador2 es:", División_round)
print("El exponente de operador1 y operador2 es:", operador_1**operador_2)
print("La división entera de operador1 y operador2 es:", operador_1//operador_2)
