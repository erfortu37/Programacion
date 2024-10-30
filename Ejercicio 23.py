# Ejercicio 23. Modifica el programa anterior para establecer si la nota es un
# excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o
# insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar
# elif sin operadores lógicos.

nota=float(input("Dime que nota has sacado en el último exámen:"))

if nota<10 and nota>=8.5:
    print("Has sacado un excelente")
elif nota<=8.4 and nota>=6.5:
    print("Has sabcado un notable")
elif nota<06.4 and nota>5:
    print("Has sacado un satisfactorio")
elif nota<5:
    print("Tienes un insuficiente")
else:
    print("error")
