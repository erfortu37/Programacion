"""
85. Te piden realizar un programa en que gestionen la media y la mediana de varias de tres 
asignaturas de legua: catalán, inglés y castellano. Una vez introducidos varios registros el 
programa debe mostrar la media y mediana los todos los alumnos introducidos
"""

cas=[]
cat=[]
ing=[]
nº_cas=0
nº_cat=0
nº_ing=0
media_cas=0
media_cat=0
media_ing=0
var=0
var_while=1
Nombre=""

while var<var_while:
    Nombre=input("Introduce el nombre de el alumno: ")
    nota_cas=int(input(f"Introduce la nota de {Nombre} en castellano: "))
    cas.append(nota_cas)
    nota_cat=int(input(f"Introduce la nota de {Nombre} en catalán: "))
    cat.append(nota_cat)
    nota_ing=int(input(f"Introduce la nota de {Nombre} en inglés: "))
    ing.append(nota_ing)
    s_n=input("¿Deseas introducir a otro estudiante?(s/n): ")
    if s_n=="s":
        var=0
    if s_n=="n":
        var=1

print(f"Notas castellano: {cas}")
print(f"Notas catalán: {cat}")
print(f"Notas inglés: {ing}")

lon_cas=len(cas)
lon_cat=len(cat)
lon_ing=len(ing)

nº_cas=sum(cas)
nº_cat=sum(cat)
nº_ing=sum(ing)

media_cas=nº_cas/lon_cas
media_cat=nº_cat/lon_cat
media_ing=nº_ing/lon_ing

r_med_cas=round(media_cas, 2)
r_med_cat=round(media_cat, 2)
r_med_ing=round(media_ing, 2)
print(f"La media en castellano es: {r_med_cas}")
print(f"La media en catalán es: {r_med_cat}")
print(f"La media en inglés es: {r_med_ing}")

cas.sort()
cat.sort()
ing.sort()

for_lon_cas__2=lon_cas-2
for_lon_cas__1=lon_cas-1
for_lon_cat__2=lon_cat-2
for_lon_cat__1=lon_cas-1
for_lon_ing__2=lon_ing-2
for_lon_ing__1=lon_ing-1

if lon_cas%2==0:
    for x in (int(for_lon_cas__2)):
        cas.pop(x)
        cas.reverse()
        x=0
    med_sum_cas=sum(cas)
    med_cas=med_sum_cas/2    
else:
    for x in (int(for_lon_cas__1)):
        cas.pop(x)
        cas.reverse()
        x=0
    med_cas=cas

if lon_cat%2==0:
    for y in (int(for_lon_cat__2)):
        cat.pop(x)
        cat.reverse
        y=0
    med_sum_cat=sum(cat)
    med_cat=med_sum_cat/2
else:
    for y in (int(for_lon_cat__1)):
        cat.pop(y)
        cat.reverse()
        y=0
    med_cat=cat

if lon_ing%2==0:
    for z in (int(for_lon_ing__2)):
        ing.pop(z)
        ing.reverse()
        z=0
    med_sum_ing=sum(ing)
    med_ing=med_sum_ing/2
else:
    for z in (int(for_lon_ing__1)):
        ing.pop(z)
        ing.reverse()
        z=0
    med_ing=ing

print(f"La mediana en castellano es: {med_cas}")
print(f"La mediana en catalán es: {med_cat}")
print(f"La mediana en inglés es: {med_ing}")