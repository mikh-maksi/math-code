# !/usr/bin/python3
from tkinter import *
root = Tk()
 
xn = 750
yn = 750
step = 50
xlc = ((xn/step)%2)*step/2
ylc = ((yn/step)%2)*step/2


c = Canvas(root, width=xn+10, height=yn, bg='white') # Размер и цвет холста
c.pack()


#Вісь X
c.create_line(0, yn/2, xn, yn/2, fill='gray',
                width=5, arrow=LAST, dash=(10,2),
                activefill='#AA0000',
                arrowshape="10 20 10")

#Вісь Y
c.create_line( xn/2, yn, xn/2, 3, fill='gray',
                width=5, arrow=LAST, dash=(10,2),
                activefill='lightgreen',
                arrowshape="10 20 10")

#Проміжні лінії
for i in range(max(int(xn/step),int(yn/step))):
    c.create_line(0, i*step+ylc, yn, i*step+ylc)
    c.create_line(i*step+xlc, 0, i*step+xlc, yn)

for y in range(max(int(xn/step),int(yn/step))):
    for x in range(int(xn/step)):
        c.create_text(xn+22+(x-int(xn/step))*step+xlc, 0+yn-10+(y-int(yn/step))*step+ylc, text=f"({x-int(xn/step/2)};{-y+int(yn/step/2)})", 
                    justify=LEFT, font="Verdana 8")

def vector(x1,y1,x2,y2,color):
    c.create_line(500+x1*100, 500-y1*100, 500+x2*100, 500-y2*100, fill=color,
                width=5, arrow=LAST, dash=(10,2),
                activefill='lightgreen',
                arrowshape="10 20 10")
    
 
root.mainloop()