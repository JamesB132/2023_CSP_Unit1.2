# a121_catch_a_turtle.py
#-----import statements-----

import turtle as trtl
import random as rand
import turtle as score_writer
import turtle as counter
import leaderboard as lb


#-----game configuration----

trgt_color = "LightSteelBlue1"
trgt_size = 2
image = "img.png"
screen = trtl.Screen()
trgt_shape = "circle"
score = 0
font_setup = ("TimesNewRoman", 20, "normal")
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

leaderboard_file_name = "a122_leaderboard.txt"
player_name = input("What is your name?")

#-----initialize turtle-----


trgt = trtl.Turtle()
trgt.speed(100)
trgt.fillcolor(trgt_color)
trgt.shapesize(trgt_size)
trgt.shape(trgt_shape)

#-----game functions--------

score_writer.penup()
score_writer.hideturtle()
score_writer.goto(330, 350)
score_writer.pendown()

counter = trtl.Turtle()
counter.penup()
counter.hideturtle()
counter.goto(-330, 350)
counter.pendown()

def trgt_clicked (x, y):
    trgt.penup()
    trgt.hideturtle()
    change_position()
    trgt.showturtle()
    trgt.pendown()

def change_position ():
    update_score()
    rand.randint(-380,380)
    new_xpos = rand.randint(-380,380)
    new_ypos = rand.randint(-380,380)
    trgt.goto(new_xpos, new_ypos)


#-----game functions-----
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
    if timer_up == True:
        trgt.hideturtle()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

def update_score():
  global score
# gives this function access to the score that was created above
  score += 1
  score_writer.clear()
  score_writer.write(score, font=font_setup)

#-----events----------------
def manage_leaderboard():

  global score
  global trgt

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, trgt, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, trgt, score)

trgt.onclick(trgt_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()