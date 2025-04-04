lista=[]
listnum=[]
listletr=[]
listnum_noduplicados=[]
listletr_noduplicados=[]
listsum=[]
May=[]
a=input()
lista=a.split("-")
for recorrer in lista:
    if recorrer.isnumeric():
        listnum.append(int(recorrer))
    elif recorrer.isalpha():
        listletr.append(recorrer)
    else:
        listnum.append(float(recorrer))

for cont in listnum:
    if cont not in listnum_noduplicados:
        listnum_noduplicados.append(cont)

listnum_noduplicados.sort()

for palabra in listletr:
    if palabra not in listletr_noduplicados:
        listletr_noduplicados.append(palabra)
        
listletr_noduplicados.sort()
for may in listletr_noduplicados:
    if may.islower():
        var=may.upper()
        May.append(var)

        
listsum=sum(listnum_noduplicados)
print(f"Valores numéricos antes de eliminar duplicados: {listnum}")
print(f"Valores numéricos después de eliminar duplicados: {listnum_noduplicados}")
print(f"Suma total después de eliminar duplicados: {listsum}")
print(f"Valores no numéricos antes de eliminar duplicados: {listletr}")
print(f"Valores no numéricos después de eliminar duplicados: {May}")