
from turtle import Turtle, Screen

timmy = Turtle()

def move_forward():
    timmy.forward(30)


screen = Screen()
screen.listen()
screen.onkey(move_forward, "space")    #here move forward is a function it is work under another function , thats why its called higher order 


screen.exitonclick()

