lista=[]
lista_2=[]
lista_3=[]
lista_4=[]
listmax=[]
f=0
g=1
h=2
a=input()
lista=a.split()
if len(lista)==1:
    while f<g:
        b=input()
        if b.isnumeric():
            lista_2=b.split()
            if len(lista_2)==1:
                c=input()
                if c.isnumeric():
                    lista_3=c.split()
                    f=1
            else:
                f=1
elif len(lista)==2:
    while g<h:
        d=input()
        if d.isnumeric():
            lista_4=d.split()
            g=2
for recorrer in lista:
    listmax.append(int(recorrer))
if len(lista)==1:
    for cont in lista_2:
        listmax.append(int(cont))
    for contador in lista_3:
        listmax.append(int(contador))
elif len(lista)==2:
    for contas in lista_4:
        listmax.append(int(contas))
list_max=max(listmax)
print(list_max)
