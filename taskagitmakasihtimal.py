from random import choice
from time import sleep

Denemesayisi=int(input('Deneme sayısı\n'))

ai1kazanma=Beraberlik=ai2kazanma=0

taskagitmakas=['tas','kagıt','makas']

for i in range(Denemesayisi):
    ai1=choice(taskagitmakas)
    ai2=choice(taskagitmakas)

    if ai1=='tas':
        if ai2=='tas':
            Beraberlik=Beraberlik + 1
        elif ai2=='kagıt':
            ai2kazanma= ai2kazanma + 1
        elif ai2=='makas':
            ai1kazanma= ai1kazanma + 1
    
    if ai1=='kagıt':
        if ai2=='tas':
            ai1kazanma=ai1kazanma+1
        elif ai2=='kagıt':
            Beraberlik= Beraberlik + 1
        elif ai2=='makas':
            ai2kazanma=ai2kazanma + 1

    if ai1=='makas':
        if ai2=='tas':
            ai2kazanma= ai2kazanma+1
        elif ai2=='kagıt':
            ai1kazanma= ai1kazanma+1
        if ai2=='makas':
            Beraberlik= Beraberlik+1

ai2kazanmaoranı=ai2kazanma/Denemesayisi*100
ai1kazanmaoranı=ai1kazanma/Denemesayisi*100
Beraberlikoranı=Beraberlik/Denemesayisi*100
print("Aİ2 KAZANMA ORANI=%{0}, Aİ1 KAZANMA ORANI=%{1}, BERABERLİK ORANI=%{2}, DENEME SAYISI={3}".format(ai2kazanmaoranı,ai1kazanmaoranı,Beraberlikoranı,Denemesayisi))
print("Aİ2 KAZANMA = {0}, Aİ1 KAZANMA = {1}, BERABERLİK = {2}".format(ai2kazanma, ai1kazanma, Beraberlik))
