# 43. Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima 
# por pantalla cada letra.

a=input()
lon=len(a)

for recorrer in range(lon):
    print(f"La letra numero {recorrer+1} es la letra {a[recorrer]}")