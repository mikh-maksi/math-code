# !/usr/bin/python3
from tkinter import *
root = Tk()
 
c = Canvas(root, width=450, height=300, bg='white') # Размер и цвет холста
c.pack()
 

def top_pert(x,y,min,max,i):
    c.create_oval(x-20,y-20,x+20,y+20)
    c.create_text(x, y+5, text=f"{max}/{min}",  font="Arial 10")
    c.create_text(x, y-10, text=f"[{i}]",  font="Arial 8")


# edge(175,75,75,175)
tops = [
    {'x':50,'y':150,'n':'1','tmax':0,'tmin':0},
    {'x':200,'y':250,'n':'2','tmax':0,'tmin':0},
    {'x':200,'y':150,'n':'3','tmax':0,'tmin':0},
    {'x':300,'y':50,'n':'4','tmax':0,'tmin':0},
    {'x':400,'y':150,'n':'5','tmax':0,'tmin':0},
]

tops_t = [
    {'tmax':0,'tmin':0},
    {'tmax':0,'tmin':0},
    {'tmax':0,'tmin':0},
    {'tmax':0,'tmin':0},
    {'tmax':0,'tmin':0},
]




def edge_kn(n1,n2,k,n):
    global tops, m_sm
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
    

    print(f"{n1}/{n2}={tops[n2]['tmax']}-{tops[n1]['tmax']} +{m_sm[n1][n2]}={tops[n2]['tmax'] - (tops[n1]['tmax']+m_sm[n1][n2])}")
    if tops[n2]['tmax'] - (tops[n1]['tmax']+m_sm[n1][n2]) >0:
        print (f"n1={n1},n2 = {n2}")
        c.create_line(x_1, y_1,x_2, y_2, fill='green',
                width=5, arrow=LAST, 
                activefill='lightgreen',
                arrowshape="10 20 10")
    else:
        c.create_line(x_1, y_1,x_2, y_2, fill='red',
                width=5, arrow=LAST, 
                activefill='lightgreen',
                arrowshape="10 20 10")       

    
        # edge_kn_green(n1,n2,'a',m_sm[n1][n2])
  
    # print(f"{n2}/{n1}")
    # print(tops[n2]['tmax'])
    # print(tops[n1]['tmax'])
    # n_c1 = tops[n2]['tmax'] 
    # n_c2 = tops[n1]['tmax']
    # n_c3 = m_sm[n1][n2]
    


    x_t = x_1+int((x_2-x_1)/2)
    y_t = y_1+int((y_2-y_1)/2)+10
    # print(f"{x_t},{y_t}")
    # c.create_text(x_t, y_t, text=k,  font="Arial 12")
    c.create_text(x_t, y_t-20, text=n,  font="Arial 12")




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
    # print(v)

    for i in range(len(m_sm[v])):
        if m_sm[v][i]>0:
            q.append(i)
            n_max[i] = n_max[v] + m_sm[v][i]
            if  n_min[i]==0 or (n_min[i]> n_min[v] + m_sm[v][i]):
                n_min[i] = n_min[v] + m_sm[v][i]

# print(m_sm)

for i in range(len(tops)):
    tops[i]['tmin'] = n_min[i]
    tops[i]['tmax'] = n_max[i]
    top_pert(tops[i]['x'],tops[i]['y'],tops[i]['tmin'],tops[i]['tmax'],i)

# print(tops_t)

for i in range(len(m_sm)):
  for j in range(len(m_sm[i])):
     if m_sm[i][j] != 0:
         edge_kn(i,j,'a',m_sm[i][j])
        #  print(f"{i},{j}")

print(tops)
for i in range(len(tops)):
    if tops[i]['tmax'] - tops[i]['tmin'] >0:
        print(f"-->{tops[i]}")


root.mainloop()

# Ребра top1_top2, які top2_max - l =top1_max - критичні.