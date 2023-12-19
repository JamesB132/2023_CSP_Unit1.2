import turtle as trtl
'''
x = starting distance
y = incremental distance
Loop:
    go forward x
    turn left 90 degrees
    go forward x + y
    turn left 90 degrees
'''
trtl.speed(10)
x = 15
y = 5
trtl.left(90)
trtl.width(5)

def Door():
    trtl.forward(10)
    trtl.penup()
    trtl.forward(x * 2)
    trtl.pendown()


def Spiral():
    global x, y
    for spirals in range(25):
        trtl.forward(x + y)
        trtl.left(90)
        y += 20
    trtl.hideturtle()
Spiral()

wn = trtl.Screen()
wn.mainloop()