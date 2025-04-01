# Ejercicio 26. Realiza un programa que, al introducir una letra por teclado, aparezca
# por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o
# False a la condición.

letra=input("Introduce una letra:")

if letra.isupper()==True:
    print("La letra está en mayúscula")
if letra.isupper()==False:
    print("La letra está en minúscula")
