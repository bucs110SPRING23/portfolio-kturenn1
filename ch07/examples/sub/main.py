# look in the current folder for the file/module
# look in python installed modules
# look in th python library

import point
import random
import turtle
import pygame

# import sub.module
# from sub.module import x

p1 = point.Point()
p2 = point.Point(3,4,"blue")

p1.xcoor = 10

print(p1.xcoor, p1.ycoor, p1.color, type(p1), id(p1))
print(p2.xcoor, p2.ycoor, p2.color, type(p2), id(p2))

points = []
for p in range(10):
    x = random.randint(0,100)
    y = random.randint(0,100)
    points.append(point.Point("red"))

t = turtle.Turtle()
for p in points:
    p.random_color()
    t.color(p.color)
    t.goto(p.xcoor, p.ycoor)

turtle.Screen().exitonclick()

pygame.init()
display = pygame.display.set_mode((500,500))

p3 = point.LED(x = 100, y = 100)

pygame.draw.circle(display, p3.color, (p3.rect.x, p3.rect.y), p3.radius)

while True:
    pygame.display.flip()