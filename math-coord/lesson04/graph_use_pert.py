# !/usr/bin/python3
from tkinter import *
root = Tk()
 
c = Canvas(root, width=450, height=300, bg='white') # Размер и цвет холста
c.pack()
 

def top(x,y,n):
    c.create_oval(x-20,y-20,x+20,y+20)
    c.create_text(x, y, text=n,  font="Arial 20")



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
    {'x':50,'y':150,'n':'1'},
    {'x':200,'y':250,'n':'2'},
    {'x':200,'y':150,'n':'3'},
    {'x':300,'y':50,'n':'4'},
    {'x':400,'y':150,'n':'5'},

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


def edge_k(n1,n2,k):
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
                width=5, arrow=LAST, 
                activefill='lightgreen',
                arrowshape="10 20 10")
    x_t = x_1+int((x_2-x_1)/2)
    y_t = y_1+int((y_2-y_1)/2)+15
    print(f"{x_t},{y_t}")
    c.create_text(x_t, y_t, text=k,  font="Arial 20")

def edge_kn(n1,n2,k,n):
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
                width=5, arrow=LAST, 
                activefill='lightgreen',
                arrowshape="10 20 10")
    x_t = x_1+int((x_2-x_1)/2)
    y_t = y_1+int((y_2-y_1)/2)+10
    print(f"{x_t},{y_t}")
    # c.create_text(x_t, y_t, text=k,  font="Arial 12")
    c.create_text(x_t, y_t-20, text=n,  font="Arial 12")


def edge_no(n1,n2):
    global tops
    x1 = tops[n1]['x']
    y1 = tops[n1]['y']
    x2 = tops[n2]['x']
    y2 = tops[n2]['y']


    if x1>x2:
        x_1 = x1-20
        x_2 = x2 + 20
    
    elif x1<x2:
        x_1 = x1+20
        x_2 = x2 - 20
    
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
                width=5, dash=(10,2),
                activefill='lightgreen',
                arrowshape="10 20 10")
# edge_no(1,2)
# edge_no(0,1)
# edge_no(2,0)
# edge_no(2,3)

m_sm = [
    [0,4,3,0,0],
    [0,0,0,0,3],
    [0,0,0,1,3],
    [0,0,0,0,3],
    [0,0,0,0,0]
] 


q = []
n_max = [0,0,0,0,0]
n_min = [0,0,0,0,0]
q.append(0)
while len(q)>0:
    v = q.pop(0)
    print(v)

    for i in range(len(m_sm[v])):
        if m_sm[v][i]>0:
            q.append(i)
            n_max[i] = n_max[v] + m_sm[v][i]
            if  n_min[i]==0 or (n_min[i]> n_min[v] + m_sm[v][i]):
                n_min[i] = n_min[v] + m_sm[v][i]


print(n_max)
print(n_min)
        

# print(len(m_sm))

for i in range(len(m_sm)):
  for j in range(len(m_sm[i])):
     if m_sm[i][j] != 0:
         edge_kn(i,j,'a',m_sm[i][j])
         print(f"{i},{j}")

# edge_kn(0,2,'a',3)
# edge_kn(0,1,'b',4)
# edge_kn(1,4,'c',3)
# edge_kn(2,3,'e',3)
# edge_kn(2,4,'d',1)
# edge_kn(3,4,'f',3)


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