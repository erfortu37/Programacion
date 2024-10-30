# Ejercicio 27. Mejora el programa anterior para controlar que el valor introducido
# es una letra y en caso de introducir un número, aparezca un aviso por pantalla.

letra=input("Introduce una letra:")

if letra.isupper()==True:
    print("La letra está en mayúscula")    
elif letra.islower()==True:
    print("La letra está en minúscula")
else:
    print("error")
