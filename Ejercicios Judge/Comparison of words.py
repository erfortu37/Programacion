lista=[]
a=input()
A=a.lower()
lista=A.split()

if lista[0]==lista[1]:
    print(f"{lista[0]} = {lista[1]}")
elif lista[0]>lista[1]:
    print(f"{lista[0]} > {lista[1]}")
elif lista[0]<lista[1]:
    print(f"{lista[0]} < {lista[1]}")