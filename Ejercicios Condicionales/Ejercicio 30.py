# Ejercicio 30. Realiza un programa que controle si la longitud de una frase
# introducida por teclado es igual, menor o mayor de 11 caracteres. Utiliza elif.

f=input("Introduce una frase:")

ff=len(f)

if ff<11:
    print("Tine menos de 11 caracteres")
elif ff>11:
    print("Tiene más de 11 caracteres")
elif ff==11:
    print("Tiene 11 caracteres")
