# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 13:25:49 2025

@author: FortunatoBenitoÈric
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

a=input("Quieres el orden ascendente(a) o descendente(d)")
if a=="a":
    listnum.reverse()
    listletr.reverse()

    print(listnum)
    print(listletr)
if a=="d":
    print(listnum)
    print(listletr)

