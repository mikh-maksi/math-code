from tkinter import *
root = Tk()
 
# Визначаємо колір
c = Canvas(root, width=200, height=200, bg='white')
c.pack()

#Демонстрація напрямку координатної прямої y
c.create_line(20, 0, 20, 100, 
                    fill='red',  width=5, arrow=LAST, activefill='#AA0000',  arrowshape="10 20 10")



root.mainloop()