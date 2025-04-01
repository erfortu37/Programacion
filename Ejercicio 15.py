# Ejercicio 15. Utiliza el valor Pi de la librería math para calcular el área y
# volumende un cilindro, introduciendo por teclado el valor de radio y altura.
# Resultado con 2 decimales.

import math

r=float(input("Introduce el radio del cilindro:"))
h=float(input("Introduce la altura del cilindro:"))

A=2*math.pi*r*(r+h)
V=math.pi*(r**2)*h

total_V=round(V, 2)
total_A=round(A, 2)

print("El área del cilindro es:", total_A)
print("El volumen del cilindro es:", total_V)
