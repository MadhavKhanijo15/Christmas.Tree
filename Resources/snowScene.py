import turtle

def position(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def star(size,color):
    turtle.color(color)
    turtle.begin_fill()

    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

    turtle.end_fill()

def light(size,color):
    turtle.color(color)
    turtle.begin_fill()

    turtle.circle(size)

    turtle.end_fill()

turtle.Screen()
turtle.setup(1000,1000)
turtle.bgpic('trees.png')

# Begin editing the code below this line ------>
position(-50,50)
star(50,'yellow')
position(150,150)
light(100,'blue')

