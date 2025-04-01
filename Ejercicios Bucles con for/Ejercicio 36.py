# Ejercicio 36. Programa que sume los n primeros n√∫meros naturales. n Lo introduce 
# el usuario.

sm=0

n=int(input("introdue un número:"))

for cont in range(n):
    sm=sm+cont

print(sm)