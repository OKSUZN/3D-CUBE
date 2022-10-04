import turtle as t



t.title("Making a 3D cube")
t.color('blue')

for i in range(4):
    t.forward(100)
    t.left(90)

t.goto(50, 50)

for i in range(4):
    t.forward(100)
    t.left(90)

t.goto(150,50)
t.goto(100,0)

t.goto(100,100)
t.goto(150,150)

t.goto(50,150)
t.goto(0,100)


t.mainloop()
