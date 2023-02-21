import random
import turtle

screen = pygame.display.set_mode()

turtle1 = turtle.Turtle()
turtle1.color("red")

turtle2 = turtle.Turtle()
turtle2.color("blue")

window = turtle.Screen()

start1 = (-100,20)
start2 = (-100,-20)

turtle1.pu()
turtle2.pu()

turtle1.goto(start1)
turtle2.goto(start2)

turtle1.pd()
turtle2.pd()

# turtle1.forward(random.randrange(1,100))
# turtle2.forward(random.randrange(1,100))

# turtle1.goto(start1)
# turtle2.goto(start2)

mylist = ["turtle1", "turtle2"]
for obj in mylist:
    turtle1.forward(random.randrange(1,10))
    turtle2.forward(random.randrange(1,10))

turtle1.goto(start1)
turtle2.goto(start2)

window.exitonclick()