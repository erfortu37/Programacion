# Ejercicio 12

lado=float(input("Dime un lado del trapecio isósceles:"))
altura=float(input("Dime la altura del trapecio isósceles:"))
base_menor=float(input("Dime la base menor del trapecio isósceles:"))
base_mayor=float(input("Dime la base mayor del trapecio isósceles:"))

print("El perímetro del trapecio isósceles es:", lado*2+base_mayor+base_menor)
print("El área del trapecio isósceles es:", (base_mayor+base_menor)*altura/2)
