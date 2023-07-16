# !/usr/bin/python3
from tkinter import *
root = Tk()
 
c = Canvas(root, width=1000, height=1000, bg='white') # Размер и цвет холста
c.pack()
 
# c.create_line(3, 3, 200, 200)
 
c.create_line(0, 500, 1000, 500, fill='gray',
                width=5, arrow=LAST, dash=(10,2),
                activefill='#AA0000',
                arrowshape="10 20 10")

c.create_line(500, 1000, 500, 3, fill='gray',
                width=5, arrow=LAST, dash=(10,2),
                activefill='lightgreen',
                arrowshape="10 20 10")

for i in range(10):
    c.create_line(0, i*100, 1000, i*100)
    c.create_line(i*100, 0, i*100, 1000)

for y in range(10):
    for x in range(10):
        c.create_text(1000+20+(x-10)*100, 0+1000-10+(y-10)*100, text=f"({x-5};{-y+5})", 
                    justify=LEFT, font="Verdana 10")

def vector(x1,y1,x2,y2,color):
    c.create_line(500+x1*100, 500-y1*100, 500+x2*100, 500-y2*100, fill=color,
                width=5, arrow=LAST, dash=(10,2),
                activefill='lightgreen',
                arrowshape="10 20 10")
    



 
