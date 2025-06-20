
from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
# print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# print(colors[0])

# riny = Turtle(shape="turtle")
# riny.color(colors[0])
# riny.penup()
# riny.goto(-220, 100)


# tiny = Turtle(shape="turtle")
# tiny.color(colors[1])
# tiny.penup()
# tiny.goto(-220, 60)


# rony = Turtle(shape="turtle")
# rony.color(colors[2])
# rony.penup()
# rony.goto(-220, 20)


# timmy = Turtle(shape="turtle")
# timmy.color(colors[3])
# timmy.penup()
# timmy.goto(-220, -20)

# johny = Turtle(shape="turtle")
# johny.color(colors[4])
# johny.penup()
# johny.goto(-220, -60)


# mohny = Turtle(shape="turtle")
# mohny.color(colors[5])
# mohny.penup()
# mohny.goto(-220, -100)

# ---------- we should redundant the lines of code ----------

y_position = [100, 60, 20, -20, -60, -100]
is_race_on = False
all_turtle_list = []

for i in range(6):
    timmy = Turtle(shape="turtle")
    timmy.color(colors[i])
    timmy.penup()
    timmy.goto(-220, y_position[i])
    all_turtle_list.append(timmy)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle_list:
        if turtle.xcor() > 220:
            is_race_on = False
            winig_color = turtle.pencolor()
            if user_bet == winig_color:
                print(f"you have won! {winig_color} is the winner")
            else:
                print(f"You lost! {winig_color} won the race")

        turtle.forward(random.randint(0, 10))
        
    


screen.exitonclick()


