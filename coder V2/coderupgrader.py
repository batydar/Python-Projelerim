import pyfiglet

batydar = pyfiglet.figlet_format("batydar")
print(batydar)

from coderdefinitaion import kodlayıcı

sayilar=["01","02","03","04","05","06","07","08","09"]
alfabe=["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z","A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z",".",","," "]
adim1=""
kodlamaliste=[]
adim2=""
a=1

for i in range(10, 61):
    sayilar.append("{}".format(i))



while a==1:
    kelime=input("kelimeyi giriniz\n")
    grup=kelime.split("/")

    if len(grup)!=2:
        a=1
    else:
        a=0


kelime = grup[0]
şifremetodu = int(grup[1])

harfsayisi=len(kelime)



for i in range(0,harfsayisi):
    harf = kelime[i]
    for a in range(0,61):
        if harf == alfabe[a]:
            if len(sayilar)<a+şifremetodu:
                a-=len(sayilar)
            adim1+=sayilar[a+şifremetodu]


şifresayıları=len(adim1)

for i in range(0, şifresayıları, 2):
    kodlamaliste.append(adim1[i]+adim1[i+1])

şifresayıları=len(kodlamaliste)

for i in range(0, şifresayıları):
    sayi = kodlamaliste[i]
    for a in range(0,61):
        if sayi == sayilar[a-1]:
            adim2+= alfabe[a-1]


print("{}/{}".format(kodlayıcı(adim2), şifremetodu))