# Ejercicio 37. Programa que pregunte cuantas notas quiero introducir y para cada nota 
# diga si estoy aprobado o suspendido.

var=int(input("¿Cuántas notas quieres introducir?"))

cont=0


for cont in range(var):
    p=int(input(f"¿Qué has sacado en este examen?"))
    susp=f"la nota {cont + 1} está suspendida"
    aprob=f"la nota{cont + 1} está aprobada"
    if p<5:
        print(susp)
    else:
        print(aprob)