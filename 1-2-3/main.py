#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)
wn.bgpic("background.gif")

apple = trtl.Turtle()
drawer = trtl.Turtle()
drawer.hideturtle()


#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_pear(active_pear):
  active_pear.shape(pear_image)
  wn.update()

def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

x = 0
y = 0
def apple_fall():
  drawer.clear()
  global x, y
  while (1 == 1):
    if y == -170:
      apple.hideturtle()
    apple.penup()
    apple.goto(x, y)
    y -= 2

def draw_an_A():
  drawer.color("white")
  drawer.write("A", font=("Arial",50, "bold"))


#-----function calls-----
draw_apple(apple)
drawer.penup()
drawer.goto(-20, -40)
draw_an_A()
wn.onkeypress(apple_fall, "a")

wn.listen()
wn.mainloop()