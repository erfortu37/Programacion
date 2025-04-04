# Sumativa Password 2.0 (Utilizando los bucles for")

# Primero explico que se pueeden elegir entre tres tipos diferentes de contraseñas (passwords) con diferentes criterios en cada una.
print("Tienes que elegir en escribir una de las tres contraseñas")
print("En la contraseña 1 has d introducir 3 números,  1 letra en minúscula, 2 letras en mayúscula y 2 caracteres especiales; En total 8 caracteres")
print("En la contraseña 2 has de introducir 1 número,  4 letras tanto mayúsculas como minúsculas y 1 caracter especial; En total 6 caracteres")
print("En la contraseña 3 has de introducir 2 números,  3 letras minúsculas y  2 caracteres especiales; En total 7 caracteres")
# Aquí pongo que la variable "num" se iguale al tipo de contraseña que se quiera poner con el int (para que lo detecte como un número) y el input (para que se pueda contestar algo al mensaje).
num=int(input("Elige que contraseña vas a poner (1, 2 o 3):"))

# Todo esto son variables que igualo a 0 para posteriormente ver el nº de números, letras, caracteres especiales, etc.
cn_num=0
cn_lmin=0
cn_lmay=0
cn_cc=0
cn_l=0
# La siguiente variable la utilizo como una "variable chivato" para posteriormente poder mostrar por pantalla si el password es correcto: (El password es correcto)
pswrd_crrct=0
# La siguiente variable la utilizo para que vaya contando las veces que el password es correcto y que al final del programa muestre por pantalla las contraseñas correctas y erróneas.
pwd_cr=0

# Estas variables las utilizo para que si hay algún error del que pona el password, que esta se modifique poniendo un comentario en el que indique que tipo de error hay.
a=""
a_=""
b=""
b_=""
c=""
c_=""
d=""
d_=""

# Como he decidido que se puedan elegir distintos criterios para el password, aquí pongo el if para que el programa se realice pero con los criterios del password tipo 1.
if num==1:
# Como se pide que el usuario ponga tres passwords, ponemos un bucle for de una variable (en este caso "f") y que se repita 3 veces in range (3)).
    for f in range (3):
# Aquí igualo la variable "password" a lo que el usuario ponga como contraseña.
        password=input("Introduce la contraseña:")
# Como tambien hemos puesto como criterio la longitud del password, hemos de medir el nº de caracteres totales que tiene la contraseña con el lon y que ese número se iguale a la variable "lon".
        lon=len(password)
        
# Aquí, si o si según el criterio, la contraseña tiene que ser 8 así que pongo el if lon==8 para que solo se realice el programa solo si la variable "lon" sea igual a 8.
        if lon==8:
# Esta es la parte más importante del programa, el bucle for. Aquí he puesto que se haga un bucle con for a la variable "cont", que irá augmentando el nº según vaya augmentando el programa, y que se repita el nº de veces de lo largo que
# sea el password. Para así poder medir el nº de números, letras, caracteres especiales, etc.
            for cont in range (lon):
# En las 2 siguientes líneas pongo que si la posición cont del password (if password[cont]) es un número, que se sume 1 unidad a la variable "cc_num". Esto sucede porque la variable "cont" empieza siendo 0 y despúes de cada
# vuelta se un número mayor, por eso, en la primera vuelta se mirará si la posición uno es un número pero en la siguienta ya será la segunda posición, etc. Tambien utilizo el método string isnumeric que lo que hace es verificar que sea
# un número, por eso pongo que si es numérico se realice la 2ª línea (if password[cont].isnumeric()==True:).
                if password[cont].isnumeric()==True:
                    cn_num=cn_num+1
# Aquí verifico primero de todo si el caracter de la vuelta que corresponda se una letra, utilizando el método string isalpha, que verifica que el caracter sea una letra, entonces si es una letra se realizarían las siguientes líneas.
# Tambien, en vez de usar el "if", utilizo el "elif" que antes de ir directamente a esa línea, mira primero si el "if" de antes se cumple o no. 
                elif password[cont].isalpha()==True:
# Despúes de verificar que el caracter correspondiente es una letra, el programa mira si es una letra mayúscula o minúscula. Para verificar que es una letra minúscula se usa el método string islower y ara verificar que es una letra
# mayúscula se usa el método string isupper. Entonces si es una letra minúscula se suma 1 unidad a la variable "cn_clmin" y si es una letra mayúscula se suma 1 unidad a la variable "cn_lmay". Aquí tambien se utiliza la misma estructura
# con el "if" y el "elif".
                    if password[cont].islower()==True:
                        cn_lmin=cn_lmin+1
                    elif password[cont].isupper()==True:
                        cn_lmay=cn_lmay+1
# Aquí ponemos que si el caracter correspondiente a la vuelta no es ni un número ni una letra, que se sume una unidad a la variable "cn_cc" para verificar que el caracter sea un caracter especial.
                else:
                    cn_cc=cn_cc+1

# Aquí finalmente, al ya haber pasado las correspondientes vueltas, ya tenemos el nº de números, letras y caracteres especiales. Con ello, aferrándonos a nuestros criterios, comparamos si hay la cantidad de cada de lo que se pide
# y que se muestre por pantala si hay algún error. Por ejemplo, si la variable "cn_num", que es la variable que mide los números, es mayor que 3 (utilizando el "if") hace que la variable "a", en este caso, como estaba vacía, ahora
# sea un mensaje poniendo que la cantidad de números es mayor a la que tocaba.
            if cn_num>3:
                a="(hay más números de los que tocan)"
# Utilizando nuestra "variable chivato" hacemos que si hay un error, que se iguale a uno.
                pswrd_crrct=1
            if cn_num<3:
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

# Finalmente se muestra por pantalla las variables modificadas o no. Entonces, si hay más números de lo normal, solo se habrá modificado la variable "a" y solo se mostrará esta ya que las otras no se muestra nada.
            print(a+a_+b+b_+c+c_+d+d_)
# Como ya se ha explicado antes, al mínimo error, la "variable chivato" se igualaba a 1. Entonces, usando el "if", si la variable es igual a 0 queriendo decir que no ha habido ningún error, se printea que el password es correcto.
# Tambien si es correcto, a la variable "pwd_cr" se le sumará 1 unidad y con eso, al final del programa sabremos las veces que la contraseña ha sido correcta.
            if pswrd_crrct==0:
                print("(El password es correcto)")
                pwd_cr=pwd_cr+1

# Aquí igualamos todas las variables que miden la cantidad de números, letras y caracteres especiales a 0 para que al hacer el bucle for de "f" no den siempre los números muy grandes y que no de error.
            cn_num=0
            cn_lmin=0
            cn_lmay=0
            cn_cc=0
            cn_l=0
            pswrd_crrct=0

# Hacemos lo mismo que con las variables anteriores, igualándolas a nada, para que si por ejemplo en la segunda vuelta haya error en la cantidad de letras, que solo muestre eso y no un mensaje de la anterior vuelta.
            a=""
            a_=""
            b=""
            b_=""
            c=""
            c_=""
            d=""
            d_=""

# Este "esle" va en relación con el "if lon==8" porque si no son los caracteres correctos, que directamente ni haga el programa y que muestre por pantalla que hay un error.
        else:
            print("No cumple con los caracteres requeridos")
        

# Este bloque es exactamente lo mismo que el anterior solo que, como los requisitos son otros, lo único que cambia, son los valores de la comparación final.
elif num==2:
    for f in range (3):
        password=input("Introduce la contraseña:")
        lon=len(password)
        
        
        if lon==6:
            for cont in range (lon):
                if password[cont].isnumeric()==True:
                    cn_num=cn_num+1
                elif password[cont].isalpha()==True:
                    cn_l=cn_l+1
                else:
                    cn_cc=cn_cc+1
                    
            if cn_num>1:
                a="(hay más números de los que tocan)"
                pswrd_crrct=1
            if cn_num<1:
                a_="(hay menos números de los que tocan)"
                pswrd_crrct=1
            if cn_l>4:
                b="(hay más letras de las que tocan)"
                pswrd_crrct=1
            if cn_l<4:
                b_="(hay menos letras de las que tocan)"
                pswrd_crrct=1
            if cn_cc>1:
                c="(hay más caracteres especiales de los que tocan)"
                pswrd_crrct=1
            if cn_cc<1:
                c_="(hay menos caracteres especiales de los que tocan)"
                pswrd_crrct=1
            
            print(a+a_+b+b_+c+c_+d+d_)
            if pswrd_crrct==0:
                print("(El password es correcto)")
                pwd_cr=pwd_cr+1
            
            cn_num=0
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
            
        else:
            print("No cumple con los caracteres requeridos")


# Este bloque es exactamente lo mismo que el anterior solo que, como los requisitos son otros, lo único que cambia, son los valores de la comparación final.
elif num==3:
    for f in range (3):
        password=input("Introduce la contraseña:")
        lon=len(password)
        
        
        if lon==7:
            for cont in range (lon):
                if password[cont].isnumeric()==True:
                    cn_num=cn_num+1
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
            if cn_lmin>3:
                b="(hay más letras minúsculas de las que tocan)"
                pswrd_crrct=1
            if cn_lmin<3:
                b_="(hay menos letras minúsculas de las que tocan)"
                pswrd_crrct=1
            if cn_lmay>0:
                c="(hay más letras mayúsculas de las que tocan)"
                pswrd_crrct=1
            if cn_cc>2:
                d="(hay más caracteres especiales de los que tocan)"
                pswrd_crrct=1
            if cn_cc<2:
                d_="(hay menos caracteres especiales de los que tocan)" 
                pswrd_crrct=1
            
            print(a+a_+b+b_+c+c_+d+d_)
            if pswrd_crrct==0:
                print("(El password es correcto)")
                pwd_cr=pwd_cr+1
            
            cn_num=0
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
            
        else:
            print("No cumple con los caracteres requeridos")

# Este "else" se relaciona con el "if" y los "elif" de la varaible "num". Eso quiere decir que este "esle" dice que si la variable "num" no es ningun tipo de conrtraseña, que muestre por pantalla que el usuario no ha escogido ningún
# tipo de contraserña para poner.
else:
    print("No has elegido ninguna password")

# Con la variable "pwd_cr" hemos medido el nº de veces que el usuario ha introducido un password correcto. Con eso, sabiendo que el usuario solamente ha puesto 3 contraseñas, podemos a la vez calcular las contraseñas que el usuario ha
# introducido incorrectamente. Así que aquí ponemos que si "pwd_cr" es igual a 0, hay 0 passwords correctas y 3 incorrectas.
if pwd_cr==0:
    print("Hay 0 passwords corectas")
    print("Hay 3 passwords incorrectas")

# Relacionado con las líenas anteriores, podemos ver que si "pwd_cr" es igual a 1, hay 1 password correcta y 2 incorrectas.
if pwd_cr==1:
    print("Hay 1 password correcta")
    print("Hay 2 passwords incorrectas")

# Relacionado con las líenas anteriores, podemos ver que si "pwd_cr" es igual a 2, hay 2 passwords correctas y 1 incorrecta.
if pwd_cr==2:
    print("Hay 2 passwords correctas")
    print("Hay 1 password incorrecta")

# Relacionado con las líenas anteriores, podemos ver que si "pwd_cr" es igual a 3, hay 3 passwords correctas y 0 incorrectas.
if pwd_cr==3:
    print("Hay 3 passwords correctas")
    print("Hay 0 passwords incorrectas")
