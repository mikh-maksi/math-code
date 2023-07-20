import tk_mult as m

for x in range(400):
    for y in range(400):
        if m.set2(x,y) ^ m.set1(x,y):
            m.c.create_line(x,y,x,1+y, fill = 'red') 

m.border()
m.root.mainloop()