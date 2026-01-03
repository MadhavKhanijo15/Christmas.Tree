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
# --- STARS ON TOP ---

# Right tree star (Aligned with large peak)
position(218, 305)
star(60, "yellow")

# Left tree star (Aligned with smaller peak)
position(-315, 235)
star(45, "yellow")

# --- LIGHTS (Yellow) ---

# Spread out to avoid overlapping with future ornaments
right_lights = [
    (215, 250), (160, 200), (280, 200), # Tier 1
    (140, 80), (218, 80), (320, 80),    # Tier 2
    (100, -60), (220, -60), (360, -60)  # Tier 3
]

left_lights = [
    (-315, 180), (-360, 130), (-270, 130),
    (-400, 40), (-315, 30), (-230, 40)
]

for x, y in right_lights + left_lights:
    position(x, y)
    light(10, "yellow")

# --- ORNAMENTS (Round & Square) ---

# Strategically placed in gaps between lights
# format: (x, y, shape_type)
all_ornaments = [
    # Right Tree
    (190, 150, "circle"), (250, 150, "square"), 
    (160, 20, "square"), (280, 20, "circle"), (220, 0, "square"),
    (140, -120, "circle"), (310, -120, "circle"), (220, -160, "square"),
    # Left Tree
    (-315, 100, "circle"), (-350, 0, "square"), (-280, 0, "circle")
]

for x, y, shape in all_ornaments:
    position(x, y)
    if shape == "circle":
        light(15, "blue")
    else:
        square(18, "red") # Using basic red for variety
