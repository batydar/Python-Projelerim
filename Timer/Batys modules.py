import time as zaman
import random
import string

def passwordgenerator():
    şifrestr=""
    şifre=[]
    harflist=list(string.ascii_lowercase)
    user_input=int(input("Şifrede bulunmasını istediğiniz harf sayısı\n"))
    user_input1=int(input("Şifrede bulunmasını istediğiniz rakam sayısı\n"))
    for i in range(0, user_input):
        birharf=random.choice(harflist)
        şifre.append(birharf)
    for i in range(0, user_input1):
        birsayi=random.randint(0,9)
        şifre.append(str(birsayi))
    
    for i in range(0, user_input+user_input1):
        rastgelehane=random.choice(şifre)   
        şifrestr=şifrestr+rastgelehane
        şifre.remove(rastgelehane)
    

    print(şifrestr)



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
