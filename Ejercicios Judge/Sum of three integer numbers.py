lista=[]
listsum=[]
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
            c=input()
            if c.isnumeric():
                f=1
                lista_c=c.split()
elif len(lista)==2:
    while g<h:
        c=input()
        if c.isnumeric():
            lista_3=c.split()
            g=2
    
for recorrer in lista:
    listsum.append(int(recorrer))
if len(lista)==1:
    for cont in lista_2:
        listsum.append(int(cont))
    for contas in lista_c:
        listsum.append(int(contas))
elif len(lista)==2:
    for contador in lista_3:
        listsum.append(int(contador))

suma=sum(listsum)

print(suma)