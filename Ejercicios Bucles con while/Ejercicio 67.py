"""
67. Realiza de nuevo el programa de Password (fase 2). El password debe tener las siguientes 
consideraciones:

Debe tener una longitud entre 6 y 8 caracteres.
Debe contener como mínimo:
2 números mayores o iguales que 1 y menor o igual que 5
2 letras minúsculas
1 letra mayúscula
2 símbolos (*, _, @, &,/,#)
1 número mayor o igual que 6 y menor o igual que 5
"""

print("Tienes que escribir una contraseña de 8 caracteres y que cumpla las siguientes condiciones:")
print("Ha de tener 2 numeros iguales o mayores a 1 y menores o iguales a 5")
print("Ha de tener 2 letras minúsculas y 1 letra mayuscula")
print("Ha de tener 2 símbolos (*, _, @, &,/,#)")
print("Y ha de tener 1 número mayor o igual que 6 y menor o igual que 5")

cn_num=0
cn_num_2=0
cn_lmin=0
cn_lmay=0
cn_cc=0
cn_l=0
pswrd_crrct=0

a=""
a_=""
b=""
b_=""
c=""
c_=""
d=""
d_=""
e=""
e_=""

password=input("Introduce la contraseña: ")
lon=len(password)

if lon==8:
    for cont in range (lon):
        if password[cont].isnumeric()==True:
            if password[cont]>1 or password[cont]==1:
                if password[cont]<5 or password[cont]==5:
                    cn_num=cn_num+1
        if password[cont].isnumeric()==True:
            if password[cont]>6 or password[cont]==6 or password[cont]<5 or password[cont]==5:
                    cn_num_2=cn_num_2+1
        elif password[cont].isalpha()==True:
            if password[cont].islower()==True:
                cn_lmin=cn_lmin+1
            elif password[cont].isupper()==True:
                cn_lmay=cn_lmay+1
        else:
            cn_cc=cn_cc+1
        
        if cn_num>2:
            a="(hay más números de los que tocan)"
            pswrd_crrct=1
        if cn_num<2:
            a_="(hay menos números de los que tocan)"
            pswrd_crrct=1
        if cn_lmin>1:
            b="(hay más letras minúsculas de las que tocan)"
            pswrd_crrct=1
        if cn_lmin<1:
            b_="(hay menos letras minúsculas de las que tocan)"
            pswrd_crrct=1
        if cn_lmay>2:
            c="(hay más letras mayúsculas de las que tocan)"
            pswrd_crrct=1
        if cn_lmay<2:
            c_="(hay menos letras mayúsculas de las que tocan)"
            pswrd_crrct=1
        if cn_cc>2:
            d="(hay más caracteres especiales de los que tocan)"
            pswrd_crrct=1
        if cn_cc<2:
            d_="(hay menos caracteres especiales de los que tocan)" 
            pswrd_crrct=1
        if cn_num_2>1:
            d="(hay más caracteres especiales de los que tocan)"
            pswrd_crrct=1
        if cn_num_2<1:
            d_="(hay menos caracteres especiales de los que tocan)" 
            pswrd_crrct=1
    print(a+a_+b+b_+c+c_+d+d_+e+e_)
    if pswrd_crrct!=1:
        print("Contraseña correcta")
    else:
        print("así que contraseña incorrecta")
else:
    ("No has introducido los caracteres correctos")
    print(a+a_+b+b_+c+c_+d+d_+e+e_)
    if pswrd_crrct!=1:
        print("Contraseña correcta")
    else:
        print("así que contraseña incorrecta")