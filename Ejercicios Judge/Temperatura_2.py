t=int(input())
if t<10 and t>=1:
    print("it's cold")
elif t<=0:
    print("it's cold")
    print("water would freeze")
elif t>30 and t<=99:
    print("it's hot")
elif t>=100:
    print("it's hot")
    print("water would boil")
elif t>=10 and t<=30:
    print("it's ok")