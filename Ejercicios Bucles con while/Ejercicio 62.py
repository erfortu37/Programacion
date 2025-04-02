
"""
62. Realiza un programa que pida dos números por teclado y presente por pantalla qué números 
hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.
"""

num_1=int(input("Introduce un número: "))
num_2=int(input("Introduce otro número: "))

par=""
impar=""

if num_1<=num_2:
    rang=(num_1,num_2)
else:
    rang=(num_2,num_1)
for a in rang:
    if a%2==0:
        par=par+f"{str(a)}-"
    elif a%2==1:
        impar=impar+f"{str(a)}-"

print(f"Los numeros pares són: {par[0:len(par)-1]}")
print(f"Los numeros impares són: {impar[0:len(impar)-1]}")