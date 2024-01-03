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
randomnum = 0
ds = 0
bs = 0
trtl.speed(0)
path_width = 15
wall_length = 5
trtl.left(90)
trtl.width(6)
iteration = 0
def Door():
    global ds, path_width
    trtl.forward(10)
    trtl.penup()
    trtl.forward(path_width * 3)
    trtl.pendown()
def Barrier():
    global bs, path_width
    trtl.forward(40)
    trtl.left(90)
    trtl.forward(path_width * 2.5)
    trtl.back(path_width * 2.5)
    trtl.right(90)
def Spiral():
    global path_width, wall_length, iteration, ds, bs, randomnum
    for spirals in range(25):
        trtl.penup()
        if iteration > 3:
            trtl.pendown()
        randomnum = rand.randint(0,1)
        if randomnum == 0:
            Door()
            Barrier()
        if randomnum == 1:
            Barrier()
            Door()
        trtl.forward(path_width + wall_length)
        trtl.left(90)
        wall_length += 20
        iteration += wall_length
    trtl.hideturtle()
Spiral()

wn = trtl.Screen()
wn.mainloop()