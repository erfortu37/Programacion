# Ejercicio 25. Repite el programa número 23 pero en esta ocasión utilizando
# operadores lógicos.

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
