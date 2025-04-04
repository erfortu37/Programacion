a=input()
var=""
var2=""
f=0
g=1
while f<g:
    if a.isalpha():
        f=1
        if a.isupper():
            var=a.lower()
            print(var)
        elif a.islower():
            var2=a.upper()
            print(var2)
