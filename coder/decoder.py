şifrelikelime=input("Şifrelenmiş kelimeyi giriniz: \n")

harfliste=[]
sayiliste=[]
kelime=""

çözümlemesayiliste=["01","02","03","04","05","06","07","08","09"]
çözümlemeharfliste=["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z","A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z",".",","," "]

for i in range(10, 61):
    çözümlemesayiliste.append("{}".format(i))

sayilar=len(şifrelikelime)

for i in range(0, sayilar, 2):
    sayiliste.append(şifrelikelime[sayilar-i-2]+şifrelikelime[sayilar-i-1])

sayilar = len(sayiliste)

for i in range(0, sayilar):
    sayi = sayiliste[i]
    for a in range(0,61):
        if sayi == çözümlemesayiliste[a-1]:
            kelime+= çözümlemeharfliste[a-1]


print(kelime)