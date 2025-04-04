# Ejercicio Sumariva Password.

c0=""
c1=""
c2=""
c3=""
c4=""
c5=""
c6=""
c7=""

var_password_correcto=1

print("Introduce una password teniendo en cuenta que:")
print("El 1º caracter tiene que ser major o igual a 1 y menor o igual a 5")
print("El 2º caracter tiene que ser una letra minúscula")
print("El 3º caracter tiene que ser una letra mayuscula")
print("El 4º caracter tiene que ser * o _ o @")
print("El 5º caracter tiene que ser una letra minúscula")
print("El 6º caracter tiene que ser major o igual a 6 y menor o igual a 9")
print("El 7º caracter tiene que ser & o / o #")
print("El 8º caracter tiene que ser menor o igual a 5")

password=input("Introduce tu password:")

# Utilizo el método string del lenght para medir la longitud de la password
caracteres=len(password)
if caracteres<6 or caracteres>8:
    print(f"Error, el password té una longitud de {caracteres} caràcters i no"
          "compleix els requisits")
# Aquí, tengo que poner el int enla varable "password[0]" para que detecte que es un
# número, no una letra. Tambien utilizo el método string isnumeric()==True para
# que lo detecte como un número.
if password[0].isnumeric()==True:
    if int(password[0])==0 or int(password[0])>6:
        c0="“Error en el caràcter 1”"
        var_password_correcto=0
else:
    c0="“Error en el caràcter 1”"
    var_password_correcto=0

# Aquí utilizo el método string del islower()==False para que si detecte que es una 
# mayúscula ponga error.
if password[1].islower()==False:
    c1="“Error en el caràcter 2”"
    var_password_correcto=0

# Aquí utilizo el método string del isupper()==False para que detecte que si es
# una minúscula ponga error.
if password[2].isupper()==False:
    c2="“Error en el caràcter 3”"
    var_password_correcto=0

# Aquí tengo que poner un "and" en vez de "or" para que el programa salga bien
if password[3]is not "_" and password[3]is not "*" and password[3]is not "@":
    c3="“Error en el caràcter 4”"
    var_password_correcto=0

# Aquí utilizo el mismo método que en el 2º caracter.
if password[4].islower()==False:
    c4="“Error en el caràcter 5”"
    var_password_correcto=0

# Aquí utilizo el mismo método que en el 1º caracter.
if password[5].isnumeric()==True:
    if int(password[5])<6 or int(password[5])>9:
        c5="“Error en el caràcter 6”"
        var_password_correcto=0
else:
    c5="“Error en el caràcter 6”"
    var_password_correcto=0

# Aquí utlizo el mismo método que en el 4º caracter.
if caracteres>6:
    if password[6]is not "&" and password[6]is not "/" and password[6]is not "#":
        c6="“Error en el caràcter 7”"
        var_password_correcto=0
# Aquí utilizo el mismo método que en el 1º y 6º caracter.
if caracteres==8:
    if password[7].isnumeric()==True:
        if int(password[7])>6:
            c7="“Error en el caràcter 8”"
            var_password_correcto=0
    else:
        c7="“Error en el caràcter 8”"
        var_password_correcto=0

if var_password_correcto==1:
    print("El format del PASSWORD és correcte")

error=c0+c1+c2+c3+c4+c5+c6+c7
print(error)
