#   a123_apple_1.py
import turtle as trtl
import random as rand
#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"
L = ""
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)
wn.bgpic("background.gif")
Letters = ["a", "b", "c", "e", "w", "q", "r", "t", "y", "u", "i", "o", "p", "z", "x", "v", "n", "m", "s", "d", "f", "g", "h", "j", "k", "l"]
random_index = 0
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
on = 1
int = 0
def reset_apple():
  global x, y, int
  apple.hideturtle()
  int = rand.randint(-100,100)
  apple.goto(int, 0)
  x = int
  y = 0
  apple.showturtle()
  choose_random_letter()
  draw_the_letter()
def apple_fall():
  drawer.clear()
  global x, y, on
  on = 1
  while (on == 1):
    if y == -170:
      apple.hideturtle()
      on = 0
      reset_apple()
    apple.penup()
    apple.goto(x, y)
    y -= 5

def draw_the_letter():
  drawer.goto(int - 12, -45)
  drawer.color("white")
  drawer.write(L, font=("Arial",50, "bold"))

def choose_random_letter():
  global random_index, L
  random_index = rand.randint(0,len(Letters)-1)
  L = Letters[random_index]
  Letters.pop(random_index)

def A():
  global L
  if L == "a":
    apple_fall()

def S():
  global L
  if L == "s":
    apple_fall()

def D():
  global L
  if L == "d":
    apple_fall()

def F():
  global L
  if L == "f":
    apple_fall()

def G():
  global L
  if L == "g":
    apple_fall()

def H():
  global L
  if L == "h":
    apple_fall()

def J():
  global L
  if L == "j":
    apple_fall()

def K():
  global L
  if L == "k":
    apple_fall()

def l():
  global L
  if L == "l":
    apple_fall()

def Q():
  global L
  if L == "q":
    apple_fall()

def W():
  global L
  if L == "w":
    apple_fall()

def E():
  global L
  if L == "e":
    apple_fall()

def R():
  global L
  if L == "r":
    apple_fall()

def T():
  global L
  if L == "t":
    apple_fall()

def Y():
  global L
  if L == "y":
    apple_fall()

def U():
  global L
  if L == "u":
    apple_fall()

def I():
  global L
  if L == "i":
    apple_fall()

def O():
  global L
  if L == "o":
    apple_fall()

def P():
  global L
  if L == "p":
    apple_fall()

def Z():
  global L
  if L == "z":
    apple_fall()

def X():
  global L
  if L == "x":
    apple_fall()

def C():
  global L
  if L == "c":
    apple_fall()

def V():
  global L
  if L == "v":
    apple_fall()

def B():
  global L
  if L == "b":
    apple_fall()

def N():
  global L
  if L == "n":
    apple_fall()

def M():
  global L
  if L == "m":
    apple_fall()




#-----function calls-----
draw_apple(apple)
drawer.penup()
drawer.goto(-20, -40)
choose_random_letter()
draw_the_letter()
wn.onkeypress(A, "a")
wn.onkeypress(S, "s")
wn.onkeypress(D, "d")
wn.onkeypress(F, "f")
wn.onkeypress(G, "g")
wn.onkeypress(H, "h")
wn.onkeypress(J, "j")
wn.onkeypress(K, "k")
wn.onkeypress(l, "l")
wn.onkeypress(Q, "q")
wn.onkeypress(W, "w")
wn.onkeypress(E, "e")
wn.onkeypress(R, "r")
wn.onkeypress(T, "t")
wn.onkeypress(Y, "y")
wn.onkeypress(U, "u")
wn.onkeypress(I, "i")
wn.onkeypress(O, "o")
wn.onkeypress(P, "p")
wn.onkeypress(Z, "z")
wn.onkeypress(X, "x")
wn.onkeypress(C, "c")
wn.onkeypress(V, "v")
wn.onkeypress(B, "b")
wn.onkeypress(N, "n")
wn.onkeypress(M, "m")


wn.listen()
wn.mainloop()