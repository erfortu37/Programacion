"""
75. Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por 
pantalla los siguientes resultados:
a. Cantidad total de valores
b. Cantidad de números
c. Cantidad de letras
d. Cantidad de mayúsculas
e. Suma de los valores numéricos
"""
may=0
letra=0
num=0
suma=0
lista1=['a','b','D','x','r','X','3','h','w','2','i']

lon=len(lista1)
print(f"Número de valores: {lon}")

for recorrer in (lista1):
    if recorrer.isnumeric():
        num=num+1
        suma=suma+int(recorrer)
    elif recorrer.isalpha():
        letra=letra+1
        if recorrer.isupper():
            may=may+1

print(f"Cantidad de números: {num}")
print(f"Cantidad de letras: {letra}")
print(f"Cantidad de mayúsculas: {may}")
print(f"Suma total de los números: {suma}")