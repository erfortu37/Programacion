pares=0
impares=0
for cont in range(50):
    if cont%2==0:
        pares=pares+1
    else:
        impares=impares+1

print("Numero de pares: ", pares)
print("numero de impares: ", impares)