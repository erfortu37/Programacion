# Ejercicio 28. Mejora el programa anterior para controlar también la introducción de
# símbolos. Utiliza elif.

a=input("Introduce algo:")

if a.isupper()==True:
    print("La letra está en mayúscula")    
elif a.islower()==True:
    print("La letra está en minúscula")
elif a.isnumeric()==True:
    print("Es un número")
elif a.isdigit()==False:
    print("Es un símbolo")
