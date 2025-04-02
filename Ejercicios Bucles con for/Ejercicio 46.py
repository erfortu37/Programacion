"""
46. A partir del programa anterior, soluciona el error que se produce en el test anterior con la 
palabra Abrigo utilizando únicamente una instrucción.
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