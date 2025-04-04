# Vamos a hacer un juego de adivinanzas con los bucles con while

import random

v=random.randint(1, 5)

q=20
while q<30:
    res=int(input("Intenta acertar el número en el que pienso del 1 al 5:"))
    if res ==v:
        print(f"Has acertado, el número era {v}")
        q=35
    else:
        print("Vuelve a intentarlo")