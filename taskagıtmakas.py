import random
import time



Oyuncukazanma=0
aiKazanma=0

liste1=['tas','kagıt','makas']

a=1
b=1
while a==1:
    aisecim=random.choice(liste1)
    print('Tas')
    time.sleep(1)
    print('Kagıt')
    time.sleep(1)
    print('Makas')
    time.sleep(1)
    oyuncusecim=input("Tas/Kagıt/Makas\n")
    
    print("Oyuncu x Bilgisayar\n{} x {}".format(oyuncusecim, aisecim))
    if oyuncusecim=='Tas' or oyuncusecim=='tas':
        if aisecim=='tas':
            print('Berabere')
        elif aisecim=='makas':
            print("Oyuncu kazandı")
            Oyuncukazanma = Oyuncukazanma +1
        else:
            print('Bilgisayar Kazandı')
            aiKazanma = aiKazanma +1
        
    if oyuncusecim=='kagıt' or oyuncusecim=='Kagıt':
        if aisecim=='tas':
            print('Oyuncu Kazandı')
            Oyuncukazanma = Oyuncukazanma +1
        elif aisecim=='kagıt':
            print('Berabere')
        else:
            print('Bilgisayar kazandı')
            aiKazanma = aiKazanma +1
        
    if oyuncusecim=='Makas' or oyuncusecim=='makas':
        if aisecim=='tas':
            print('Bilgisayar kazandı')
            aiKazanma = aiKazanma +1
        elif aisecim=='kagıt':
            print('Oyuncu Kazandı')
            Oyuncukazanma = Oyuncukazanma +1
        else:
            print('Berabere')




    print("Oyuncu {0}/{1} Bilgisayar".format(Oyuncukazanma,aiKazanma))
    tamamdevam=input('Bitir/Devam\n')
    if tamamdevam=='Bitir':
        a=0

