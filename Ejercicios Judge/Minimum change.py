bn_500=0
bn_200=0
bn_100=0
bn_50=0
bn_10=0
bn_20=0
bn_5=0
cn_2=0
cn_1=0
cn_0_5=0
cn_0_20=0
cn_0_10=0
cn_0_05=0
cn_0_02=0
cn_0_01=0
listnum=[]
listnum2=[]
lista=[]
a=input()
lista=a.split()
eur=0
moned=0


for recorrer in (lista[:-1]):
    listnum.append(int(recorrer))
    for element in listnum:
        eur=element
lista.reverse()
for cont in (lista[:-1]):
    listnum2.append(cont)
    for t in listnum2:
        moned=t
while eur<0 or moned<0:
    while bn_500!=0:
        