"""
76. A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras 
y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás 
en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo.
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