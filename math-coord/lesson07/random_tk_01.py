# https://docs.python.org/uk/3/library/random.html

import math
from tkinter import *
import random
import time
root = Tk()

c = Canvas(root, width=200, height=200, bg='green') # Размер и цвет холста
c.pack()

c.create_rectangle(50, 50, 150, 150,outline="#fb0",fill="#ddd")


def kub(n):
    if n == 0:
        c.create_rectangle(50, 50, 150, 150,outline="#fb0",fill="#ddd")
    if n == 1:
        c.create_oval(95,95,105,105,fill = "black")
    if n == 2:
        c.create_oval(60,60,70,70,fill = "black")
        c.create_oval(130,140,140,130,fill = "black")
    if n == 3:
        c.create_oval(60,60,70,70,fill = "black")
        c.create_oval(95,95,105,105,fill = "black")
        c.create_oval(130,140,140,130,fill = "black")
    if n == 4:
        c.create_oval(60,60,70,70,fill = "black")
        c.create_oval(60,140,70,130,fill = "black")
        c.create_oval(130,60,140,70,fill = "black")
        c.create_oval(130,140,140,130,fill = "black")
    if n == 5:
        c.create_oval(60,60,70,70,fill = "black")
        c.create_oval(60,140,70,130,fill = "black")
        c.create_oval(130,60,140,70,fill = "black")
        c.create_oval(130,140,140,130,fill = "black")
        c.create_oval(95,95,105,105,fill = "black")
        
    if n == 6:
        c.create_oval(60,60,70,70,fill = "black")
        c.create_oval(60,140,70,130,fill = "black")
        c.create_oval(60,95,70,105,fill = "black")
        c.create_oval(130,60,140,70,fill = "black")
        c.create_oval(130,95,140,105,fill = "black")
        c.create_oval(130,140,140,130,fill = "black")

for i in range(10):
    n = random.randint(1, 6)
    print(n)
    kub(0)
    root.update()
    kub(n)
    root.update()
    time.sleep(1)

root.mainloop()

