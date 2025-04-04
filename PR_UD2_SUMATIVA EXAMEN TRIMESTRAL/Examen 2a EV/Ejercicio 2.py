lista=[]
a=input()
lista=a.split()
b=input("Qué palabra quieres buscar?")
count_var=lista.count(b)
print(lista)
print(f"La palabra {b} aparcece {count_var} vez/ces")
join_frase=", ".join(lista)
print(join_frase)