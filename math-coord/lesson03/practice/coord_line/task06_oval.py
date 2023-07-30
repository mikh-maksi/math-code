from tkinter import *
root = Tk()
 
# Визначаємо колір
c = Canvas(root, width=200, height=200, bg='white')
c.pack()

#Вісь по середині
c.create_line(0, 100, 200, 100, 
                    fill='red',  width=5, arrow=LAST, activefill='#AA0000',  arrowshape="10 20 10")

c.create_text(185, 80, text='X', font="Verdana 10")

# Намалюємо крапку із фоном
c.create_oval(95, 95, 105, 105, outline="red", fill="green", width=2)

root.mainloop()