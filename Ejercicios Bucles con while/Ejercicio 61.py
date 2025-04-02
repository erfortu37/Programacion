"""
61. A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es
superior o igual a 40
"""

var=0
mult=1

num=int(input("Introduce un numero: "))
print(f"La tabla del numero {num} es:")

while var<10:
    tot=num*mult
    print(tot)
    mult=mult+1
    var+=1
    
    if tot>=40:
        var=10
print("Fin del programa")