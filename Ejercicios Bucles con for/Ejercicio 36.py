# Ejercicio 36. Programa que sume los n primeros números naturales. n Lo introduce 
# el usuario.

sm=0

n=int(input("introdue un n�mero:"))

for cont in range(n):
    sm=sm+cont

print(sm)