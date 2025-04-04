# Ejercicio1.py (SUMATIVA)

print("Sin plomo 95")
print("Sin plomo 98")
print("Gasóleo A")
print("Gasóleo A+")
tipo=int(input(print("Escoja el tipo de combustible:")))

SP95=1.765
SP98=1.913
GSA=1.746
GSAA=1.839

if tipo==1:
    lit=int(input(print("Introduzca el número de litros a respostar:")))
    total=lit*SP95
    print(f"El total a pagar es {total}")
    
elif tipo==2:
    lit=int(input(print("Introduzca el número de litros a respostar:")))
    total=lit*SP98
    des=total*0.9
    print(f"El total a pagar es {total} y con el descuento {des}")
    
elif tipo==3:
    lit=int(input(print("Introduzca el número de litros a respostar:")))
    total=lit*GSA
    print(f"El total a pagar es {total}")
    
elif tipo==4:
    lit=int(input(print("Introduzca el número de litros a respostar:")))
    total=lit*GSAA
    des=total*0.88
    print(f"El total a pagar es {total} y con el descuento {des}")
    
else:
    print("no has escogido ningún tipo de combustible")
