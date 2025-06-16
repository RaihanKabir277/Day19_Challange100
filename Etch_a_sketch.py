
from turtle import Turtle, Screen

timmy = Turtle()

def move_forward():
    timmy.forward(50)

def move_backward():
    timmy.backward(50)

def clock_wise():
    # timmy.left(10)
    timmy.setheading(timmy.heading() + 10)

def counter_clock():
    # timmy.right(10)
    timmy.setheading(timmy.heading() - 10)

def clear_s():
    timmy.reset()

screen = Screen()
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(clock_wise, "a")
screen.onkey(counter_clock, "d")
screen.onkey(clear_s, "c")


screen.exitonclick()
