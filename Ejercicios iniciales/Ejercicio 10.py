# Ejercicio 10. Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar.

var_1=int(input("Dime un valor:"))
var_2=int(input("Dime un valor:"))

División=round(var_1/var_2, 0)

print("El cociente es:", División)
resto=var_1%2
print("El resto es:", resto)

if resto==0:
    print("El dividendo es par")
else:
    print("El dividendo es impar")



    
    

