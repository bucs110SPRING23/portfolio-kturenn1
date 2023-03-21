import turtle

window = turtle.Screen()
window.bgcolor("black")

pen = turtle.Turtle()
pen.color('yellow')
pen.up()
pen.setpos(30, 30)
pen.down()

len = input("what is the length of the picture frame? ")
wid = input("what is the width of the picture frame? ")
thick = input("what is the thickness of the picture frame? ")
color = input("what color would you like the frame to be? ")

def square(x, y, z, col):
    pen.color(col)
    # x = width
    # y = height
    # z = thickness
    # col = color

    count = 0
    for count in range(0,4):
        if count % 2 == 0:
            pen.forward(int(y))
            pen.left(90)
            count += 1

        else:
            pen.forward(int(x))
            pen.left(90)
            count += 1

    pen.up()
    pen.left(90)
    pen.forward(int(z))
    pen.left(270)
    pen.down()

    count2 = 0
    for count2 in range(0,4):
        if count2 == 0:
            pen.forward(int(y)-int(z))
            pen.left(90)
            count2 += 1

        elif count2 == 1:
            pen.forward(int(x)-(2*(int(z))))
            pen.left(90)
            count2 += 1

        elif count2 == 3:
            pen.forward(int(y)-(2*(int(z))))
            pen.left(90)
            count2 += 1

        else:
            pen.forward(int(x)-(2*(int(z))))
            pen.left(90)
            count2 += 1

def can_we_banana():
    if int(len) > 150 and int(wid) > 150:
        print("We can banana!")
        banana_time()
    else:
        print("no banana")
    
def banana_time():
    square(int(len), int(wid), int(thick), str(color))

    pen.color('yellow')
    pen.up()
    pen.forward(90)
    pen.left(90)
    pen.forward(90)
    pen.down()

    angle = 0
    pen.up()
    while angle < 90:
        pen.forward(10)
        pen.left(10)
        angle += 10
        
    pen.down()
    while angle < 180:
        pen.forward(10)
        pen.left(10)
        angle += 10



can_we_banana()


window.exitonclick()