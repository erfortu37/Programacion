t=int(input())
if t<10:
    print("it's cold")
    if t==0 or t<0:
        print("water would freeze")
elif t>30:
    print("it's hot")
    if t==100 or t>100:
        print("water would boil")
elif t>10 and t<30:
    print("it's ok")