# !/usr/bin/python3
from tkinter import *
root = Tk()
 
c = Canvas(root, width=340, height=240, bg='white') # Размер и цвет холста
c.pack()

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
st1 =set()
st2 =set()
for x in range(400):
    for y in range(400):
        if set1(x,y):
            # print(list([x,y]))
            st1.add(f"{x}-{y}")
        if set2(x,y):
            st2.add(f"{x}-{y}")

# st = st1 
# st = st1.union(st2)
# st = st1.difference(st2) 
st = st1 ^ st2 

for el in st:
    x = int(el.split('-')[0])
    y = int(el.split('-')[1])
    c.create_line(x,y,x,1+y, fill = 'red') 
    
root.mainloop()


