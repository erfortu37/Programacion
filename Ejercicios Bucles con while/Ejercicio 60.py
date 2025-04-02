
"""
60. Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. 
Utiliza únicamente el while.
"""

var=0
mult=1

num=int(input("Introduce un numero: "))
print(f"La tabla del numero {num} es:")

while var<10:
    print(num*mult)
    mult=mult+1
    var+=1