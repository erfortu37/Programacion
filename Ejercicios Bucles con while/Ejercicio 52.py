# 52. Realiza un programa que sume dos números enteros por teclado y presente 
# el resultado por pantalla. El programa preguntará si deseas o no repetir la operación. Con While

a=0
while a==0:
    num_1=int(input("introduce un número entero: "))
    num_2=int(input("introduce otro número entero: "))
    
    print("La suma es", num_1+num_2)
    
    a=int(input("Quieres repetir la operación (0=sí ; cualquier número=No): "))