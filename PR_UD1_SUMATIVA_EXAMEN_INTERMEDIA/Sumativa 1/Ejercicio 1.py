# Ejercicio 1 (Sumativa)

# El error está en que antes del input tiene que haver un {float(} para que se puedan
# sumar numeros decimales. Al poner esto, se tiene que añadir otro {)} final.
var_1=float(input("Introduce el primer número:"))

# En esta línea se produce el mismo error de antes. Tambien hay un nuevo error, la
# frase que está dentro del paréntesis del input, tiene que estar entre comillas.
var_2=float(input("Introduce el segundo número:"))

# En esta línea hay varios errores. El primero está al principio del todo, con el
# {var total}, este, tiene que ir unido, ya sea por un {_} o lo que sea. El segundo
# error está en que no se ponen bien las variables. En vez de poner var_1 + var_2
# se ha puesto var1 + var 2.
var_total=var_1 + var_2

# En esta línea, el primer error está en que var_1 y var_2 tienen que estar entre
# llaves {}. Otro error es que delante de la f, no tiene que haver una coma. El otro
# error está en que el total, se tiene que poner var_total, y tiene que estar separado
# de la frase por una coma.
print(f"el resultado de sumar {var_1} y {var_2} es:", var_total)
