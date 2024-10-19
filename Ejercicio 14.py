# Ejercicio 14. Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.
import math
diámetro=float(input("Dime el diámetro de un círculo:"))


área=((diámetro/2)**2)*math.pi
perímetro=(diámetro/2)*(math.pi*2)

área_r=round(área, 1)
perímetro_r=round(perímetro, 1)

print("El área del círculo es:", área_r)
print("El perímetro del círculo es:", perímetro_r)
