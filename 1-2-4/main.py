import turtle as trtl
import random as rand
'''
x = starting distance
y = incremental distance
Loop:
    go forward x
    turn left 90 degrees
    go forward x + y
    turn left 90 degrees
'''
ds = 0
ds = 0
trtl.speed(0)
x = 15
y = 5
trtl.left(90)
trtl.width(6)
iteration = 0
def Door():
    global ds
    trtl.forward(ds)
    trtl.penup()
    trtl.forward(x * 3)
    trtl.pendown()

def Barrier():
    global bs
    trtl.forward(br)
    trtl.left(90)
    trtl.forward(x * 2.5)
    trtl.back(x * 2.5)
    trtl.right(90)


def Spiral():
    global x, y, iteration, ds, bs
    for spirals in range(25):
        ds = rand.randint(x * 2, (y - x * 2))
        bs = rand.randint(x * 2, (y - x * 2))
        trtl.penup()
        if iteration > 3:
            trtl.pendown()
        Door()
        Barrier()
        trtl.forward(x + y)
        trtl.left(90)
        y += 20
        iteration += 1
    trtl.hideturtle()
Spiral()

wn = trtl.Screen()
wn.mainloop()