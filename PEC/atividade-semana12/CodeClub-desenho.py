
from turtle import *


def drawSquare():
    pendown()
    begin_fill()
    for side in range(4):
        forward(64)
        left(90)
    end_fill()
    penup()


def drawStar(size, cor):
    color(cor)
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(size)
    end_fill()
    penup()


def drawPlanets(size, cor):
    color(cor)
    pendown()
    begin_fill()
    for _ in range(360):
        forward(size)
        right(1)
    end_fill()
    penup()


color("Red")
bgcolor("MidnightBlue")
speed(11)

drawSquare()
forward(100)
drawSquare()
left(90)
forward(150)
drawSquare()
backward(200)
drawStar(50, "orange")
backward(200)
drawStar(100, "green")
forward(150)
right(90)
backward(200)
drawPlanets(1, "red")
backward(200)
drawPlanets(2, "orange")
hideturtle()
done()



