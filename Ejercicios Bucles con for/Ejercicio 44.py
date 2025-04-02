"""
44. Realiza un programa que recorra todos los números comprendidos de 0 a 100 realizando saltos 
de 3 en 3. El resultado debe aparecer por pantalla en una línea con los números separados por ‘,’
"""
num=""
for x in range(100):
    if x%3==0:
        num=",".join(int(x))

print(num)