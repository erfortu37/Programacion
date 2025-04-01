# 41. Imprime el siguiente patrón utilizando for:

a="54321"
lon=len(a)
for cont in range(lon):
    print(a)
    a=a[1:len(a)]