# !/usr/bin/python3
from tkinter import *
root = Tk()
 
c = Canvas(root, width=340, height=240, bg='white') # Размер и цвет холста
c.pack()
 
# c.create_line(3, 3, 200, 200)
 
# c.create_oval(60,60,210,210,fill='gray',dash=(3,5))
# c.create_oval(160,60,310,210,fill='gray')
def set1(x,y):
    out = 0
    if (x-120)**2+(y-120)**2<=10000:
        out = 1
    return out

def border1(x,y):
    out = 0
    if 9600<=(x-120)**2+(y-120)**2<=10000:
        out = 1
    return out

def set2(x,y):
    out = 0
    if (x-220)**2+(y-120)**2<=10000:
        out = 1
    return out

def border2(x,y):
    out = 0
    if 9600<=(x-220)**2+(y-120)**2<=10000:
        out = 1
    return out

for x in range(400):
    for y in range(400):
        if set1(x,y):
            c.create_line(x,y,x,1+y, fill = 'green')  
        if set2(x,y):
            c.create_line(x,y,x,1+y, fill = 'red') 
        if set1(x,y) and set2(x,y):
            c.create_line(x,y,x,1+y, fill = 'blue') 
        if border1(x,y) or border2(x,y):
            c.create_line(x,y,x,1+y, fill = 'black')

# c.create_oval(160,60,310,210,fill='gray')


root.mainloop()