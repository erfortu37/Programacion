# Ejercicio 51. A partir del programa anterior, modifica el código para que sea 
# el usuario quién introduzca el número de veces que desea que repita la frase 
# Buenos días. Con While

cont=0

num=int(input("Cuántas veces quieres que salga buenos días: "))
while cont<num:
    print("Buenos días")
    cont+=1