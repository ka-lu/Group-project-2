#group project 2
#Kaitlyn Lum and Anna Fong
#Date: July, 2023

import turtle

#draws a picture

#draws the ground
def groundDrawing(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(600)


#function that draws the dress
def draw_dress():
    turtle.color("#d85c64")
    turtle.penup()
    turtle.goto(-150,-200)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(300)
    turtle.left(90)
    for i in range (63):
        turtle.forward(5)
        turtle.left(1)
    turtle.setheading(270)
    turtle.forward(255)
    turtle.end_fill()
    turtle.goto(-150,-200)
    turtle.setheading(90)
    turtle.begin_fill()
    for i in range(63):
        turtle.forward(5)
        turtle.right(1)
    turtle.setheading(270)
    turtle.forward(255)
    turtle.end_fill()

#draws head of peppa
def headDrawing():
    turtle.pencolor("#ee4eaa")
    turtle.fillcolor("#ffacdc")
    turtle.penup()
    turtle.goto(0,180)
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(0)
    for i in range(310):
        turtle.right(1)
        turtle.forward(1.8)
    turtle.end_fill()

    #drawing nose
    turtle.begin_fill()
    for i in range(40):
        turtle.forward(5.5)
        turtle.right(1.5)
    for i in range(60):
        turtle.forward(1.5)
        turtle.right(1.9)

    for i in range(14):
        turtle.forward(5.5)
        turtle.right(2.6)
    turtle.end_fill()


    #drawing tip of nose
    turtle.setheading(240)
    turtle.penup()
    turtle.goto(105,219)
    turtle.pendown()
    for i in range(100):
        turtle.left(1.3)
        turtle.forward(1)

def nostrilDrawing(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.shape("circle")
    turtle.shapesize(0.5)
    turtle.color("#f48cc8")
    turtle.stamp()

def earDrawing():
    turtle.shape("classic")
    turtle.penup()
    turtle.goto(-70,145)
    turtle.pendown()
    turtle.fillcolor("#ffacdc")
    turtle.begin_fill()
    turtle.setheading(150)
    for i in range(20):
        turtle.forward(2)
        turtle.right(1.3)
    for i in range (55):
        turtle.right(2.9)
        turtle.forward(1)
    for i in range(18):
        turtle.forward(2)
        turtle.right(1.4)
    turtle.end_fill()

    #right ear
    turtle.penup()
    turtle.goto(-27,185)
    turtle.setheading(130)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(18):
        turtle.forward(2)
        turtle.right(1.1)

    for i in range (53):
        turtle.right(3.3)
        turtle.forward(1)

    for i in range(17):
        turtle.forward(2)
        turtle.right(1.4)

    turtle.end_fill()

def blush():
    turtle.penup()
    turtle.goto(-50, 80)
    turtle.pendown()
    turtle.shape("circle")
    turtle.color("#ff72c6")
    turtle.shapesize(3)
    turtle.stamp()


groundDrawing(-300,-250)
draw_dress()
headDrawing()
nostrilDrawing(120,185)
nostrilDrawing(135,188)
earDrawing()
blush()

turtle.exitonclick()