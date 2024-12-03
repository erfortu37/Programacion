# Ejercicio 38. A partir del programa anterior, establece los rangos para que el 
# usuario no pueda introducir notas inferiores a 0 y superiores a 10



var=int(input("¿Cuántas notas quieres introducir?"))

cont=0


for cont in range(var):
    p=int(input(f"¿Qué has sacado en este examen?"))
    susp=f"la nota {cont + 1} está suspendida"
    aprob=f"la nota{cont + 1} está aprobada"
    
    if p<5 and p>-1:
        print(susp)
    elif p>4 and p<11:
        print(aprob)
    else:
        print("Has introducido una nota equivocada")