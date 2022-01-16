import random
import time
from Canveatakdeğerleri import *
from Rastgeleolay import *
import pyfiglet
gversion="0.0.1, demo"

text1=pyfiglet.figlet_format("Untitled RPG")
print(text1, "\n Game by batydar" ,"\n", gversion, "\n","\n","\n")

canavar=0

def envanter():
    user_input=input("Eşya kullanacak mısınız(e/h)")
    if user_input=="e":
        user_input=input(f"1 {envaterslot1.isim}\n2 {envaterslot2.isim}\n3 {envaterslot3.isim}\n4 {envaterslot4.isim}\n5 {envaterslot5.isim}\n")
        if user_input=="1":
            user_input=input(f"kullanılacak item {envaterslot1.isim}. Doğru mu?(e/h)\n")
            if user_input=="e":
                oyuncu1.can=100
            else:
                envanter()
        elif user_input=="2":
            user_input=input(f"kullanılacak item {envaterslot2.isim}. Doğru mu?(e/h)\n")
            if user_input=="e":
                oyuncu1.can=100
            else:
                envanter()
        elif user_input=="3":
            user_input=input(f"kullanılacak item {envaterslot3.isim}. Doğru mu?(e/h)\n")
            if user_input=="e":
                oyuncu1.can=100
            else:
                envanter()
        elif user_input=="4":
            user_input=input(f"kullanılacak item {envaterslot4.isim}. Doğru mu?(e/h)\n")
            if user_input=="e" or "E":
                oyuncu1.can=100
            else:
                envanter()
        elif user_input=="5":
            user_input=input(f"kullanılacak item {envaterslot5.isim}. Doğru mu?(e/h)\n")
            if user_input=="e" or "E":
                oyuncu1.can=100
            else:
                envanter()
        else:
            envanter()
            
    elif user_input=="h" or "H":
        print()
    else:
        envanter()

def slot1seçim():
        user_input=input(f"{silahslot1.isim} ile ne yapacaksınız\n")
        if user_input=="standart saldırı":
            silahslot1.beklemesuresi=2
            tamhasar=silahslot1.hasar
            silahslot1.şarjör-=1
            kritik=100-random.randint(0,100)
            if silahslot1.kritiksans>kritik:
                tamhasar=silahslot1.hasar*silahslot1.kritikartis
                

            return tamhasar
        else:
            slot1seçim()

def slot2seçim():
    tamhasar=0
    user_input=input(f"{silahslot2.isim} ile ne yapacaksınız\n")
    if user_input=="standart saldırı":
        tamhasar=silahslot2.hasar
        kritik=100-random.randint(0,100)
        if silahslot2.kritiksans>kritik:
            tamhasar=silahslot2.hasar*silahslot2.kritikartis

        return tamhasar
    else:
        slot2seçim()

def silahseçim():
    user_input=input(f"{saldırgan1.isim}'a hangi silahınız ile saldırı yapacaksınız?\n {silahslot1.isim}, {silahslot2.isim}\n")
    if user_input==silahslot1.isim:
        if silahslot1.beklemesuresi==0:
            return slot1seçim()
        else:
            print(f"Tabancayı kullanmanıza {silahslot1.beklemesuresi} tur var")
    elif user_input==silahslot2.isim:
        return slot2seçim()
    else:
        silahseçim()

def turgeçme():
    if silahslot1.beklemesuresi>0:
        silahslot1.beklemesuresi-=1 


oyuncu1=oyuncu()
silahslot1 = tabanca()
silahslot1.beklemesuresi=0
silahslot2 = bıçak()
envaterslot1=caniksiri()
envaterslot2=caniksiri()
envaterslot3=caniksiri()
envaterslot4=caniksiri()
envaterslot5=caniksiri()


olay=random.randint(1,1)

if olay==1:
    Rastgeleolay1()
    canavar=1




while canavar==1:
    hasar=silahseçim()
    saldırgan1.can-=hasar
    oyuncu1.can-=saldırgan1.hasar
    time.sleep(1)
    print(f"{saldırgan1.hasar} kadar hasar aldınız, canınız={oyuncu1.can}")
    time.sleep(1)
    turgeçme()
    if (saldırgan1.can<=0):
        canavar=0
    envanter()