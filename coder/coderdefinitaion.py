def kodlayıcı(kelime):
    harfliste=[]
    sayiliste=[]
    şifrelikelime=""

    çözümlemesayiliste=["01","02","03","04","05","06","07","08","09"]
    çözümlemeharfliste=["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z","A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z",".",","," "]

    for i in range(10, 61):
        çözümlemesayiliste.append("{}".format(i))


    harfler=len(kelime)

    for i in range(0, harfler):
        harfliste.append(kelime[harfler-i-1])

    for i in range(0, harfler):
        harf = harfliste[i]
        for a in range(0,61):
            if harf == çözümlemeharfliste[a-1]:
                şifrelikelime+= çözümlemesayiliste[a-1]

    return şifrelikelime