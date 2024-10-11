# Ejercicio 14
import math
diámetro=float(input("Dime el diámetro de un círculo:"))


área=((diámetro/2)**2)*math.pi
perímetro=(diámetro/2)*(math.pi*2)

área_r=round(área, 1)
perímetro_r=round(perímetro, 1)

print("El área del círculo es:", área_r)
print("El perímetro del círculo es:", perímetro_r)
