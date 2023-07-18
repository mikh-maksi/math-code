# !/usr/bin/python3
from tkinter import *
root = Tk()
 
c = Canvas(root, width=400, height=400, bg='white') # Размер и цвет холста
c.pack()
 

def top(x,y,n):
    c.create_oval(x-20,y-20,x+20,y+20)
    c.create_text(x, y, text=n,  font="Arial 25")

def edge(x1,y1,x2,y2):
    x_1 = x1-10
    y_1 = y1 +20
    x_2 = x2 + 1
    y_2 = y2 -20

    c.create_line(x_1, y_1,x_2, y_2, fill='red',
                width=5, arrow=LAST, dash=(10,2),
                activefill='lightgreen',
                arrowshape="10 20 10")

# edge(175,75,75,175)
tops = [
    {'x':50,'y':50,'n':'a'},
    {'x':250,'y':50,'n':'b'},
    {'x':50,'y':250,'n':'c'},
    {'x':250,'y':250,'n':'d'},

]

def edge_n(n1,n2):
    global tops
    x1 = tops[n1]['x']
    y1 = tops[n1]['y']
    x2 = tops[n2]['x']
    y2 = tops[n2]['y']


    if x1>x2:
        x_1 = x1-10
        x_2 = x2 + 10
    
    elif x1<x2:
        x_1 = x1+10
        x_2 = x2 - 10
    
    elif x1==x2:
        x_1 = x1
        x_2 = x2

    if y1 > y2:
        y_1 = y1 -20
        y_2 = y2 +20
    elif y1 < y2:
        y_1 = y1 +20
        y_2 = y2 -20
    elif y1 == y2:
        y_1 = y1 
        y_2 = y2 
        

    c.create_line(x_1, y_1,x_2, y_2, fill='red',
                width=5, arrow=LAST, dash=(10,2),
                activefill='lightgreen',
                arrowshape="10 20 10")
edge_n(1,2)
edge_n(0,1)
edge_n(2,0)
edge_n(2,3)

# беремо координати вершин. Якщо чітко під - стрілка з центра низу - в центр верху
# Якщо ліворуч - з лівого краю, якщо праворуч - з правого краю.
# Аналогічно для другої вершини.



def vector(x1,y1,x2,y2,color):
    c.create_line(500+x1*100, 500-y1*100, 500+x2*100, 500-y2*100, fill=color,
                width=5, arrow=LAST, dash=(10,2),
                activefill='lightgreen',
                arrowshape="10 20 10")

for tp in tops:
    top(tp['x'],tp['y'],tp['n'])


root.mainloop()