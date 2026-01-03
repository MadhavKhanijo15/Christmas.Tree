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
position(-316,254)
star(50,'red')
position(163,330)
star(100,'yellow')

position(100,100)
light(20,'blue')
position(170,90)
light(20,'blue')

#Make it snow, make it snow, make it snow!
turtle.tracer(0)
turtle.addshape("snowFall.gif")
turtle.speed(0)
turtle.shape("snowFall.gif")
turtle.penup()
turtle.goto(0, 500)
turtle.right(90)


while True :
    turtle.update()
    turtle.forward(0.5)
    if turtle.ycor()<-499:
        turtle.goto(0,500)






