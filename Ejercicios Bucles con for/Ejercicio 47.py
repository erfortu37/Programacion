"""
47. Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe 
mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b
"""

int_1=int(input("dime numero: "))
otr=int(input("dime numero: "))

if int_1<otr:
    r=range(int_1,otr+1)
elif int_1>otr:
    r=range(int_1,otr-1,-1)

a=""

for n in r:
    a+=f"-{n}"

a=a[1:len(a)]

print(a)
