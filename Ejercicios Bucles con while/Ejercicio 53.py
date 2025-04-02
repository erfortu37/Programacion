# 53. A partir del código anterior, haz que aparezca al finalizar el programa 
# por pantalla el total las sumas y el número de repeticiones. Con While

d=0
n=0
a=0
while a==0:
    num_1=int(input("introduce un número entero: "))
    num_2=int(input("introduce otro número entero: "))
    
    suma=num_1+num_2
    print("La suma es", suma)
    
    a=int(input("Quieres repetir la operación (0=sí ; cualquier número=No): "))
    d=d+num_1+num_2
    n+=1

print(f"La suma total es: {d} y el número de repeticiones es: {n}")