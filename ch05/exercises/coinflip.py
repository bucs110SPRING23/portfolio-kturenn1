import turtle
import random

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(0)
pen.color("orange")

wn = turtle.Screen()
wn.bgcolor("black")

distance = 10
angle = 90
is_in_screen  = True

while is_in_screen:
    coin = random.randrange(0,2)
    if coin:
        pen.right(angle)
    else:
        pen.left(angle)
    pen.forward(distance)

    turtleX = pen.xcor()
    turtleY = pen.ycor()

    x_range = wn.window_width()/2
    y_range = wn.window_height()/2

    if abs(turtleX) > x_range or abs(turtleY) > y_range:
        is_in_screen = false

wn.exitonclick()