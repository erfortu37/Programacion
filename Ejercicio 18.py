# Ejercicio 18. Cines Paradiso celebran su décimo aniversario y por ser un día
# especial realizan importantes descuentos. A los adultos se les aplicará un 10% de
# descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula
# el total a pagar introduciendo por teclado el número de menores y el número de
# adultos que asisten al cine.

entrada=12

entradas_nino=int(input("¿Cuántas entradas entradas de menores de 18 quieres comprar?"))
entradas_adulto=int(input("¿Cuántas entradas de adultos quieres comprar?"))

valor_entradas_n=(entrada * entradas_nino) * 0.5
valor_entradas_a=(entrada * entradas_adulto) * 0.9

total=valor_entradas_n+valor_entradas_a

print("El valor total es:", total)
