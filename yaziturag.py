from tkinter import *
import tkinter as tk

import random
import time


def yazitura():
        para = ["                    \n  _   _  __ _ _____ \n | | | |/ _` |_  / |\n | |_| | (_| |/ /| |\n  \__, |\__,_/___|_|\n   __/ |            \n  |___/             \n                    ","  _                   \n | |                  \n | |_ _   _ _ __ __ _ \n | __| | | | '__/ _` |\n | |_| |_| | | | (_| |\n  \__|\__,_|_|  \__,_|\n                      \n                      "]
        sc = random.choice(para)
        sonuc['text']=sc
    


pencere = tk.Tk()
pencere.geometry("300x300")
parat=tk.Button(text="Parayi at",height=5,width=10,command=yazitura)
parat.place(x=120,y=10)
sonuc = tk.Label(text=" ")
sonuc.place(x=120,y=100)
pencere.mainloop()