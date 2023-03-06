import turtle
import random

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(0)
pen.color("orange")

wn = turtle.Screen()
wn.bgcolor("black")

def is_in_screen(w, t):
    left_bound = -w.window_width()/2
    right_bound = w.window_width()/2
    top_bound = -w.window_height()/2
    bottom_bound = w.window_height()/2

    turtleX = pen.xcor()
    turtleY = pen.ycor()

    

distance = 10
angle = 90


while is_in_screen(wn, pen):
    coin = random.randrange(0,2)
    if coin:
        pen.right(angle)
    else:
        pen.left(angle)
    pen.forward(distance)

wn.exitonclick()