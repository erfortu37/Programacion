# 55. Última vez que reutilizamos el mismo código.. lo prometo . A partir del 
# programa anterior haz que sea todo exactamente igual pero teniendo en cuenta 
# que el programa se repita siempre y cuando la suma acumulada sea inferior a 50
# o la suma acumulada sea par. Con While

d=0
n=0
res=0
while d<50 and res==0:
    num_1=int(input("introduce un número entero: "))
    num_2=int(input("introduce otro número entero: "))
    
    suma=num_1+num_2
    print("El resultado de la suma es", suma)
    
    d=d+num_1+num_2
    n+=1
    res=d%2
    
    if n==1:
        print(f"El total acumulado es: {d} y llevas 1 operación realizada")
    elif n>1:
        print(f"El total acumulado es: {d} y llevas {n} operaciones realizadas")

print("Fin del programa")