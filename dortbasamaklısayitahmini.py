from random import *

a=1

binlerbasamak=randint(1,9)
yüzlerbasamak=randint(0,9)

while binlerbasamak==yüzlerbasamak:
    yüzlerbasamak=randint(0,9)

onlarbasamak=randint(0,9)

while onlarbasamak==binlerbasamak or onlarbasamak==yüzlerbasamak:
    onlarbasamak=randint(0,9)

birlerbasamak=randint(0,9)

while birlerbasamak==binlerbasamak or birlerbasamak==onlarbasamak or birlerbasamak==yüzlerbasamak:
    birlerbasamak=randint(0,9)


sayi=binlerbasamak*1000+yüzlerbasamak*100+onlarbasamak*10+birlerbasamak

deneme=0

while a==1:
    
    birlertuttu=onlartuttu=yüzlertuttu=binlertuttu=0
    binleryanlısyerde=yüzleryanlısyerde=onlaryanlısyerde=birleryanlısyerde=0
    binlerhatalı=yüzlerhatalı=onlarhatalı=birlerhatalı=0
    deneme=deneme+1


    yanlısyerde=0
    tahmin=int(input("Tahmininizi giriniz\n"))


    tahminbinlerbasamak=tahmin//1000
    tahmin=tahmin%1000
    
    tahminyüzlerbasamak=tahmin//100
    tahmin=tahmin%100
    
    tahminonlarbasamak=tahmin//10
    tahmin=tahmin%10

    tahminbirlerbasamak=tahmin
    
    
    if tahminbinlerbasamak==binlerbasamak:
        binlertuttu=1
    elif tahminbinlerbasamak==yüzlerbasamak or tahminbinlerbasamak==onlarbasamak or tahminbinlerbasamak==birlerbasamak:
        binleryanlısyerde=1
    else:
        binlerhatalı=1
    
    if tahminyüzlerbasamak==yüzlerbasamak:
        yüzlertuttu=1
    elif tahminyüzlerbasamak==binlerbasamak or tahminyüzlerbasamak==onlarbasamak or tahminyüzlerbasamak==birlerbasamak:
        yüzleryanlısyerde=1
    else:
        yüzlerhatalı=1

    if tahminonlarbasamak==onlarbasamak:
        onlartuttu=1
    elif tahminonlarbasamak==binlerbasamak or tahminonlarbasamak==yüzlerbasamak or tahminonlarbasamak==birlerbasamak:
        onlaryanlısyerde=1
    else:
        onlarhatalı=1

    if tahminbirlerbasamak==birlerbasamak:
        birlertuttu=1
    elif tahminbirlerbasamak==binlerbasamak or tahminbirlerbasamak==yüzlerbasamak or tahminbirlerbasamak==onlarbasamak:
        birleryanlısyerde=1
    else:
        birlerhatalı=1

    if binlertuttu==1:
        binlercevap="+"
    elif binleryanlısyerde==1:
        binlercevap="x"
    else:
        binlercevap="-"

    if yüzlertuttu==1:
        yüzlercevap="+"
    elif yüzleryanlısyerde==1:
        yüzlercevap="x"
    else:
        yüzlercevap="-"

    if onlartuttu==1:
        onlarcevap="+"
    elif onlaryanlısyerde==1:
        onlarcevap="x"
    else:
        onlarcevap="-"

    if birlertuttu==1:
        birlercevap="+"
    elif birlertuttu==1:
        birlercevap="x"
    else:
        birlercevap="-"

    cevap="{0}{1}{2}{3}".format(binlercevap,yüzlercevap,onlarcevap,birlercevap)


    print("{0}{1}{2}{3}".format(binlercevap,yüzlercevap,onlarcevap,birlercevap))

    if cevap=="++++":
        a=0
        print("Başardın")
    
    