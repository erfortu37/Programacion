# Ejercicio 21. Programa que calcula una ecuación de segundo grado. Controla
# que el valor de la raíz cuadrada no de un valor negativo

import math

a=int(input("Dime el término de la incógnita que se eleve al cuadrado (a):"))
b=int(input("Dime el término de la incógnita (b):"))
c=int(input("Dime el término independiente (C):"))

total=((-b + math.sqrt(b**2 - 4*a*c)) / 2*a)
total_2=((-b - math.sqrt(b**2 - 4*a*c)) / 2*a)

print("El resultado 1 es:", total)
print("El resultado 2 es:", total_2)
