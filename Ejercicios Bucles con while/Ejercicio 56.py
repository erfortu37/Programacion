# 56. Realiza un programa que gestione un establecimiento de venta de bocadillos.
# Un pedido se compone de: bocadillo, acompañamiento y bebida. Un cliente puede 
# pedir más de un pedido. El dependiente a partir del menú (ver imagen), se 
# encarga de introducir los datos. El menú solo se visualiza una vez al ejecutar
# el programa. El programa debe preguntar al dependiente tras la 
# realización de un pedido, si quiere gestionar otro. 

# El establecimiento contempla los siguientes descuentos:
# Si el total a pagar es entre 20 y 30 euros, se aplica un descuento del 5%
# Si el total a pagar es superior a 30 euros, se aplica un descuento del 15%
# Una vez se finaliza la introducción de todos los pedidos de un cliente, debe 
# aparecer por pantalla:
    
# • El número de pedidos realizados
# • Total a pagar.
# • Total con IVA (10%)
# • Total con el descuento aplicado.

ped=0
num_ped=1
syn=0
boc=0
entr=0
beb=0
total=0

print("Para pedir, el menú consta de un bocadillo, un acompañamiento y una bebida")
print("De bocadillos hay tres:")
print("Para pedir el bocadillo de calamares introduzca el nº 1 cuando se le pida.")
print("Para pedir el bocadillo de chistorra introduzca el nº 2 cuando se le pida.")
print("Para pedir el bikini de jamón introduzca el nº 3 cuando se le pida.")
print("Ahora para los entrantes, que tambien hay tres tipos:")
print("Para pedir las patatas finas introduzca el nº 1 cuando se le pida.")
print("Para pedir patatas gruesas introduzca el nº 2 cuando se le pida.")
print("Para pedir patatas rústicas introduzca el nº 3 cuando se le pida.")
print("Tambien hay tres tipos de bebida:")
print("Para pedir la Coca Cola introduzca el nº 1 cuando se le pida.")
print("Para pedir el Acuarius introduzca el nº 2 cuando se le pida.")
print("Para pedir el agua introduzca el nº 3 cuando se le pida.")
print("Si el total a pagar es de 20 a 30 euros se hará un descuento del 5%")
print("Si el total a pagar es superior a 30 euros se hará un descuento del 15%")

while ped<num_ped:
    boc=int(input("Introduzca un número según el bocadillo que quiera: "))
    if boc==1:
        total=total+9
    elif boc==2:
        total=total+4.5
    elif boc==3:
        total=total+2.5
    
    entr=int(input("Introduzca un número según el entrante que quiera: "))
    if entr==1:
        total=total+1.5
    if entr==2:
        total=total+1.75
    if entr==3:
        total=total+2
    
    beb=int(input("Introduzca un número según la bebida que quiera: "))
    if beb==1:
        total=total+2
    if beb==2:
        total=total+1.5
    if beb==3:
        total=total+1

    ped+=1
    syn=int(input("¿Quiere hacer otro pedido?(introduzca 1 si sí y introduzca cualquier otro número si no)"))
    if syn==1:
        num_ped=num_ped+1

print(f"El número de pedidos es: {ped}")
print(f"El total a pagar es: {total}")
print(f"El total con IVA es: {total+ total*0.1}")
if total>=20 and total<=30:
    print(f"El total con el descuento del 5% es: {total+total*0.1-total*0.05}")
elif total>30:
    print(f"El total con el descuento del 15% es: {total+total*0.1-total*0.15}")
