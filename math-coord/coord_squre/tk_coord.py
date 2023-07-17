# !/usr/bin/python3
import math
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

#Підпис координат
for y in range(max(int(xn/step),int(yn/step))):
    for x in range(int(xn/step)):
        c.create_text(xn+22+(x-int(xn/step))*step+xlc, 0+yn-10+(y-int(yn/step))*step+ylc, text=f"({x-int(xn/step/2)};{-y+int(yn/step/2)})", 
                    justify=LEFT, font="Verdana 8")

#Функція для малювання вектору
def vector(x1,y1,x2,y2):
    c.create_line(xn/2+x1*step, yn/2-y1*step, xn/2+x2*step, yn/2-y2*step, fill='black',
                width=5, arrow=LAST, 
                activefill='blue',
                arrowshape="10 20 10")

def vector_color(x1,y1,x2,y2,color):
    c.create_line(xn/2+x1*step, yn/2-y1*step, xn/2+x2*step, yn/2-y2*step, fill=color,
                width=5, arrow=LAST, 
                activefill='blue',
                arrowshape="10 20 10")

def vector_calc(x1,y1,x2,y2):
    #Малюємо вектор
    vector(x1,y1,x2,y2)
    #Створюємо прямокутник-підкладку під текст
    c.create_rectangle(xn-350, yn-20, xn, yn,outline="#fb0",fill="#ddd")
    # Робимо обрахунки
    modulo = math.sqrt((x2-x1)**2+(y2-y1)**2)
    cos_a = (x2-x1)/modulo
    cos_b = (y2-y1)/modulo
    # Виводимо текст на прямокутник-підкладку
    c.create_text(xn-350, yn, text=f"|a| = {format(modulo, '.3f')}, cos_a = {format(cos_a, '.3f')}, cos_b = {format(cos_b, '.3f')}", 
                    anchor=SW, font="Verdana 8")

def vector_minus(a_x1,a_y1,a_x2,a_y2,b_x1,b_y1,b_x2,b_y2):
    c_x1 = b_x2 
    c_y1 = b_y2 
    c_x2 = a_x2
    c_y2 = a_y2
    vector_color(a_x1,a_y1,a_x2,a_y2,'green')    
    vector_color(b_x1,b_y1,b_x2,b_y2,'red')
    vector_color(c_x1,c_y1,c_x2,c_y2,'blue')

def vector_mult(x1,y1,x2,y2,k):
    vector_color(x1,y1,x2,y2,'gray')
    vector_color(k*x1,k*y1,k*x2,k*y2,'gray')

def cos_fi(a_x1,a_y1,a_x2,a_y2,b_x1,b_y1,b_x2,b_y2):
    vector_color(a_x1,a_y1,a_x2,a_y2,'green')
    vector_color(b_x1,b_y1,b_x2,b_y2,'green')
    c.create_rectangle(xn-350, yn-20, xn, yn,outline="#fb0",fill="#ddd")
    a_x = a_x2-a_x1
    a_y = a_y2-a_y1
    b_x = b_x2-b_x1
    b_y = b_y2-b_y1
    s_mult = a_x*b_x+a_y*b_y
    print(f"s_mult = {s_mult}")
    modulo_a = math.sqrt(a_x**2+a_y**2)
    print(f"modulo_a = {modulo_a}")
    modulo_b = math.sqrt(b_x**2+b_y**2)
    print(f"modulo_b = {modulo_b}")
    cos = s_mult/(modulo_a*modulo_b)
    c.create_text(xn-350, yn, text=f"cos fi= {format(cos, '.3f')}, fi ={format(math.acos(cos), '.3f')} rad,  fi = {format(math.degrees(math.acos(cos)), '.3f')} grad", 
                    anchor=SW, font="Verdana 8")
