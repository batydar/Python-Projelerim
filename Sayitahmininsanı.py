from random import *
from time import *

buyukdeger=100
kucukdeger=0

a=1
deneme=0

print("Sayıyı tuttunuz mu?")
sleep(1)
tahmin=randint(0,100)

while a==1:
    print('Tuttuğunuz sayi', tahmin,'mi?')
    dogruluk=input('Buyuk/Kucuk/Dogru\n')


    if dogruluk=="Buyuk":
        kucukdeger=tahmin
        sayi=randint(tahmin,buyukdeger)
        tahmin=sayi
        sleep(1)
        deneme=deneme+1
    elif dogruluk=="Kucuk":
        buyukdeger=tahmin
        sayi=randint(kucukdeger,tahmin)
        tahmin=sayi
        sleep(1)
        deneme=deneme+1
    elif dogruluk=="Dogru":
        print("Kazandım")
        sleep(1)
        a=0
    else:
        print("Lütfen doğru değer giriniz")
        sleep(1)

print(deneme, "deneme yaptınız")