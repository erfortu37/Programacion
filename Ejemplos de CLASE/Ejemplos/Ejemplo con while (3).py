import random
num=random.randint(1,4)

minn=int(input("introduce un número del 1 al 4: "))

while num!=minn:
    minn=int(input("has fallado, introduce otro número: "))

print("Has acertado")