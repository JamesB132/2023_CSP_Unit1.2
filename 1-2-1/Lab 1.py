# Import Turtle
import turtle as trtl

# Declare Turtles.
# ONLY USE THE lines TURTLE!!!!
box = trtl.Turtle()
lines = trtl.Turtle()
wn = trtl.Screen()
sx = -490
sy = -300
ey = -300
ex = 490
lines.speed(100)

# Setup Screen
def setupScreen():
    global wn
    wn.setup(1000, 700)

# Create the box on the screen
def setupBox():
    box.speed(0)
    box.penup()
    box.goto(-490, -300)
    box.pendown()
    box.forward(980)
    box.left(90)
    box.forward(630)
    box.left(90)
    box.forward(980)
    box.left(90)
    box.forward(630)
    box.hideturtle()


# Code for 80 point version goes here
def v80():
    global sx
    global sy
    global ex
    global ey
    lines.penup()
    lines.goto(sx,sy)
    lines.pendown()
    for shape in range (90):
        lines.goto(sx, sy)
        lines.goto(ex, ey)
        sx += 98/9
        ey += 7.08

# Code for the 90 point version goes here
def v90():
    # Calling the 80 point function - don't copy-paste from earlier method!!
    v80()





# Code for the 100 point version here
def v100():
    # Calling the 90 point function - don't copy-paste from earlier method!!
    global sx
    global sy
    global ex
    global ey
    v90()






# Code for the 110 point version here
def v110():
    # Calling the 100 point function - don't copy-paste from earlier method!!
    v100()

setupScreen()
setupBox()
v110()






wn.mainloop()