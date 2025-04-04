lista=[]
listnum=[]
listmax=[]
listmin=[]
listMay=[]
promedio=0
promediototal=0
a=input()
lista=a.split("-")
for recorrer in lista:
    listnum.append(int(recorrer))
lon=len(lista)
listmax=max(listnum)
listmin=min(listnum)
promedio=sum(listnum)
promediototal=promedio/lon
for contador in listnum:
    if contador>promediototal:
        listMay.append(int(contador))

print(f"Máximo: {listmax}")
print(f"Mínimo: {listmin}")
print(f"Promedio: {promediototal}")
print(f"Nueva lista: {listMay}")