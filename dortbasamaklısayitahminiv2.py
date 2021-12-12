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

while a==1:
    tuttu=0
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
        tuttu=tuttu+1

    if tahminyüzlerbasamak==yüzlerbasamak:
        tuttu=tuttu+1

    if tahminonlarbasamak==onlarbasamak:
        tuttu=tuttu+1

    if tahminbirlerbasamak==birlerbasamak:
        tuttu=tuttu+1
    
    if tahminbinlerbasamak==yüzlerbasamak or tahminbinlerbasamak==onlarbasamak or tahminbinlerbasamak==birlerbasamak:
        yanlısyerde=yanlısyerde+1
    
    if tahminyüzlerbasamak==binlerbasamak or tahminyüzlerbasamak==onlarbasamak or tahminyüzlerbasamak==birlerbasamak:
        yanlısyerde=yanlısyerde+1

    if tahminonlarbasamak==binlerbasamak or tahminonlarbasamak==yüzlerbasamak or tahminonlarbasamak==birlerbasamak:
        yanlısyerde=yanlısyerde+1

    if tahminbirlerbasamak==binlerbasamak or tahminbirlerbasamak==yüzlerbasamak or tahminbirlerbasamak==onlarbasamak:
        yanlısyerde=yanlısyerde+1

    print("{}/{}".format(yanlısyerde,tuttu))

    if tuttu==4:
        a=0
    
    