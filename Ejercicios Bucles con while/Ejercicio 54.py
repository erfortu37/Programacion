# 54. Modifica el programa anterior y haz que se repita el ciclo automáticamente 
# hasta que el total de todas las sumas sea superior a 50, será entonces cuando 
# el programa finalice. No hará falta preguntar si deseas repetir la operación.
# En cada operación aparece por pantalla la suma de la operación y su acumulado.
# Para aquellos de vosotros que os fijáis en los detalles, controlar que el 
# mensaje del acumulado es singular o plural.. . Con While

d=0
n=0
while d<50:
    num_1=int(input("introduce un número entero: "))
    num_2=int(input("introduce otro número entero: "))
    
    suma=num_1+num_2
    print("El resultado de la suma es", suma)
    
    d=d+num_1+num_2
    n+=1
    
    if n==1:
        print(f"El total acumulado es: {d} y llevas 1 operación realizada")
    elif n>1:
        print(f"El total acumulado es: {d} y llevas {n} operaciones realizadas")

print("Fin del programa")