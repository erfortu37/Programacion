"""
45. Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string
distinguiendo vocales y las consonantes:
"""
vocales=['a','e','i','o','u','á','é','í','ú','ó']
vocal=""
conson=""

a=input()
lon=len(a)
for x in range(lon):
    if a[x] in vocales:
        vocal=vocal+a[x]
    else:
        conson=conson+a[x]
print("Las vocales son: ", vocal)
print("Las consonantes son: ", conson)