a=input()
lista_vocales=['a','e','i','o','u','A','E','I','O','U']
f=0
g=1
while f<g:
    if a.isalpha:
        f=1
        if a.isupper():
            print("uppercase")
            if a in lista_vocales:
                print("vowel")
            else:
                print("consonant")
        if a.islower():
            print("lowercase")
            if a in lista_vocales:
                print("vowel")
            else:
                print("consonant")