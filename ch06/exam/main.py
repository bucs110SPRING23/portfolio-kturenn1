import turtle

window = turtle.Screen()
window.bgcolor("black")

pen = turtle.Turtle()
pen.color('yellow')
pen.up()
pen.setpos(30, 30)
pen.down()

leng = int(input("what is the length of the picture frame? "))
thick = int(input("what is the thickness of the picture frame? "))
color = str(input("what color would you like the frame to be? "))

def square(x, z, col):
    """
    this function draws a square
    args: x = length of the square, z = thickness of the square, col = color of the square, col = color of the square
    """
    pen.color(col)
    pen.down()

    count = 0
    for count in range(0,4):
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
            pen.forward(int(x-int(z)))
            pen.left(90)
            count2 += 1

        else:
            pen.forward(int(x)-(2*(int(z))))
            pen.left(90)
            count2 += 1

def can_we_banana(a):
    """
    this function checks if the frame is big enough
    args: a = length of the frame
    """
    if a > 150:
        print("We can banana!")
        banana_time()
    else:
        print("no banana")
    
def banana_time():
    """
    this function draws the banana
    """
    square(leng, thick, color)

    pen.color('yellow')
    pen.up()
    pen.forward(120)
    pen.left(90)
    pen.forward(120)
    pen.down()

    angle = 0
    pen.up()
    while angle < 120:
        pen.forward(10)
        pen.left(10)
        angle += 10
        
    pen.down()
    while 0 < angle < 290:
        pen.forward(10)
        pen.left(10)
        angle += 10
    
    pen.left(85)
    pen.forward(10)
    pen.left(60)

    angle = 120
    while 0 < angle < 270:
        pen.forward(10)
        pen.right(10)
        angle += 10

def main():

    can_we_banana(leng)

main()


window.exitonclick()