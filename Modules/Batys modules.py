import time as zaman
import string
import random

def zarat(kaçyüzüvar, atış, tekrarlama):
    toplamort=0
    for a in range(0,tekrarlama):    
        yüzlistesi=[]
        toplam=0
        for i in range(0, atış):
            yüzlistesi.append(random.randint(1,kaçyüzüvar))
        
        for i in range(0, atış):
            """print("Atış {} sayı: {}".format(i+1, yüzlistesi[i]))"""
            toplam+=yüzlistesi[i]
        
        if kaçyüzüvar==6:
            ortdeger=toplam/atış
            toplamort+=ortdeger
            print("Ortalama = {} atış = {}".format(ortdeger,a+1))
            
    print("Ortalama = {}".format(toplamort/tekrarlama))

    
    
def passwordgenerator(harfsayi, rakamsayi, kaçşifre):
    şifreler=[]
    for a in range(0, kaçşifre):
        şifre=[]
        şifrestr=""
        harflist=list(string.ascii_lowercase)
        for i in range(0, harfsayi):
            birharf=random.choice(harflist)
            şifre.append(birharf)
        for i in range(0, rakamsayi):
            birsayi=random.randint(0,9)
            şifre.append(str(birsayi))
        
        for i in range(0, rakamsayi+harfsayi):
            rastgelehane=random.choice(şifre)   
            şifrestr=şifrestr+rastgelehane
            şifre.remove(rastgelehane)
        
        şifreler.append(şifrestr)

    return şifreler



def sayac(time):
    x=time
    second=time
    minute=0
    hour=0
    day=0
    if time>59:
        minute=time//60
        second=second-minute*60
        if minute>59:
            hour=minute//60
            minute=minute-hour*60
            if hour>23:
                day=hour//24
                hour=hour-day*24
            
    for x in range(0,time):
        print("{0}:{1}:{2}:{3}".format(day,hour,minute,second))
        if second==0:
            second+=59
            if minute==0:
                minute+=59
                if hour==0:
                    hour+=23
                    day-=1
                else:
                    hour-=1        
            else:
                minute-=1
        else:    
            second-=1
        zaman.sleep(1)
