# !/usr/bin/python3
from tkinter import *
root = Tk()
 
c = Canvas(root, width=400, height=400, bg='white') # Размер и цвет холста
c.pack()
 

def top(x,y,n):
    c.create_oval(x-25,y-25,x+25,y+25)
    c.create_text(x, y, text=n, justify=CENTER, font="Arial 30")

def edge(x1,y1,x2,y2):

    x_1 = x1-12
    y_1 = y1 +25
    x_2 = x2 + 12
    y_2 = y2 -25
    c.create_line(x_1, y_1,x_2, y_2, fill='red',
                width=5, arrow=LAST, dash=(10,2),
                activefill='lightgreen',
                arrowshape="10 20 10")

# edge(175,75,75,175)
tops = [
    {'x':175,'y':75,'n':1},
    {'x':75,'y':175,'n':2},
    {'x':275,'y':175,'n':3},
    {'x':115,'y':325,'n':4},
    {'x':235,'y':325,'n':5},
]



def edge_n(n1,n2):
    global tops
    x1 = tops[n1]['x']
    y1 = tops[n1]['y']
    x2 = tops[n2]['x']
    y2 = tops[n2]['y']


    if x1>x2:
        x_1 = x1-12
        x_2 = x2 + 12
    
    elif x1<x2:
        x_1 = x1+12
        x_2 = x2 - 12
    
    elif x1==x2:
        x_1 = x1
        x_2 = x2

    if y1 > y2:
        y_1 = y1 -25
        y_2 = y2 +25
    elif y1 < y2:
        y_1 = y1 +25
        y_2 = y2 -25
    elif y1 == y2:
        y_1 = y1 
        y_2 = y2 
        

    c.create_line(x_1, y_1,x_2, y_2, fill='red',
                width=5, arrow=LAST, dash=(10,2),
                activefill='lightgreen',
                arrowshape="10 20 10")
# edge_n(1,2)
# edge_n(0,1)
# edge_n(0,2)
# edge_n(0,3)
# edge_n(0,4)
# беремо координати вершин. Якщо чітко під - стрілка з центра низу - в центр верху
# Якщо ліворуч - з лівого краю, якщо праворуч - з правого краю.
# Аналогічно для другої вершини.



def vector(x1,y1,x2,y2,color):
    c.create_line(500+x1*100, 500-y1*100, 500+x2*100, 500-y2*100, fill=color,
                width=5, arrow=LAST, dash=(10,2),
                activefill='lightgreen',
                arrowshape="10 20 10")

# root.mainloop()