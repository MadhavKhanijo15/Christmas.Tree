import turtle
import random

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
# STARS ON TOP

# Right tree star
position(185, 315)
star(60, "yellow")

# Left tree star
position(-315, 260)
star(50, "yellow")

# LIGHTS

# Right tree lights
right = [
    (225, 170), (160, 180), (280, 180), # Top tier
    (140, 60), (220, 60), (310, 60),    # Middle tier
    (100, -80), (220, -100), (350, -80) # Bottom tier
]

# Left tree lights
left = [
    (-295, 140), (-325, 165), (-246, 165), # Top tier
    (-365, 20), (-295, 10), (-230, 20)      # Middle tier
]

for x, y in right + left:
    position(x, y)
    light(10, "yellow")

#ORNAMENTS(square+round)
# Round Ornaments
ornaments = [
    # Right Tree
    (110 , 115), (338, 115), (53, -65), (382, -65), (-40,-285), (480,-285),

    # Left Tree
    (-375, 110), (-210, 110), (-400, -13), (-165,-13), (-480,-180), (-113,-180)
]

for x, y in ornaments:
    position(x, y)
    light(15, "red")

# Square Ornaments

def square(size, color):
    turtle.penup()
    turtle.setheading(0)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

#DRAWING ORNAMENTS
def draw_ornament():
    colors = ["orange", "pink", "white"]
    color = random.choice(colors)

    shape = random.choice(["circle", "square"])

    if shape == "circle":
        light(12, color)
    else:
        square(18, color)

        # Right tree zones
right_zones = {
    "top": [(215, 200), (250, 180)],
    "middle": [(180, 120), (240, 120), (300, 110)],
    "bottom": [(160, -20), (240, -40), (320, -20)]
}

# Left tree zones
left_zones = {
    "top": [(-315, 140)],
    "middle": [(-360, 60), (-270, 60)],
    "bottom": [(-390, -40), (-240, -40)]
}

for zones in [right_zones, left_zones]:
    for zone in zones.values():
        for x, y in zone:
            position(x, y)
            draw_ornament()

#GIFTS

def gift(width, height, color):
    turtle.color(color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

# Right tree gifts
position(270, -375)
gift(60, 40, "red")

position(350, -375)
gift(50, 35, "green")

# Left tree gifts
position(-375, -250)
gift(60, 40, "blue")

position(-230, -250)
gift(50, 35, "pink")
            


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

