"""
75. Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por 
pantalla los siguientes resultados:
a. Cantidad total de valores
b. Cantidad de números
c. Cantidad de letras
d. Cantidad de mayúsculas
e. Suma de los valores numéricos
"""
listnum=[]
listletr=[]
lista1=['a','b','D','x','r','X','3','h','w','2','i']

for cont in lista1:
    if cont.isnumeric():
        listnum.append(int(cont))
    else:
        listletr.append(cont)
listnum.sort()
listletr.sort()


print(listnum)
print(listletr)

listnum.reverse()
listletr.reverse()

print(listnum)
print(listletr)