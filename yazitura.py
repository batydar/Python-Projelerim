import random
import time
a=1
while a==1:
    para=["                    \n  _   _  __ _ _____ \n | | | |/ _` |_  / |\n | |_| | (_| |/ /| |\n  \__, |\__,_/___|_|\n   __/ |            \n  |___/             \n                    ","  _                   \n | |                  \n | |_ _   _ _ __ __ _ \n | __| | | | '__/ _` |\n | |_| |_| | | | (_| |\n  \__|\__,_|_|  \__,_|\n                      \n                      "]

    sc = random.choice(para)    

    print(sc)
    time.sleep(3)
    a=0
    x = int(input("tekrardan atacak misiniz?\n1/0\n=>"))
    if (x == 1):
        a=1
    else:
        a=0


