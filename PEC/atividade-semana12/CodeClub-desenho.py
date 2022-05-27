
from turtle import *


def drawSquare():
    pendown()
    begin_fill()
    for side in range(4):
        forward(64)
        left(90)
    end_fill()
    penup()

color("Red")
bgcolor("MidnightBlue")


drawSquare()
forward(100)
drawSquare()
left(90)
forward(150)
drawSquare()

hideturtle()
done()
