# Ejercicio 22. Programa que al introducir una nota por teclado te diga si has
# aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5
# o mayor estás aprobado.

nota=float(input("Dime que nota has sacado en el último exámen:"))

if nota<5: print("Has suspendido")
elif nota>4.9: print("Has aprovado")
