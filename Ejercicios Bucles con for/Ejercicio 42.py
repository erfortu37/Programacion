# 42. Imprima el siguiente patrón con el ciclo for. 

a="*"
for cont in range(9):
    print(a)
    if cont==0:
        a="**"
    elif cont==1:
        a="***"
    elif cont==2:
        a="****"
    elif cont==3:
        a="*****"
    elif cont==4:
        a="****"
    elif cont==5:
        a="***"
    elif cont==6:
        a="**"
    elif cont==7:
        a="*"
