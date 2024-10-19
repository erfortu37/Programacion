# Ejercicio 17. Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el peso (en kg)
# y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado es igual o superior a 25, debe
# aparecer un mensaje informando de sobrepeso.

Kg=float(input("Dime cuanto pesas en Kg:"))
Alt=float(input("Dime tu altura en metros:"))

IMC=Kg/(Alt**2)

print("Tu IMC es:", IMC)
if IMC>25 or IMC==25: print("Tienes sobrepeso")
