
from turtle import *
from random import *


def drawSquare(size, cor):
    color(cor)
    pendown()
    begin_fill()
    for side in range(4):
        forward(size)
        left(90)
    end_fill()
    penup()


def drawSymbol(size, cor):
    color(cor)
    pendown()
    begin_fill()
    for _ in range(0, 3):
        forward(size)
        right(60)
        forward(size)
        right(120)
        forward(size)
        right(60)
        forward(size)
    end_fill()
    penup()


def moveToRandomLocation():
    penup()
    setpos(randint(-400, 400), randint(-400, 400))
    pendown()


bgcolor("Green")
speed(11)

for draw in range(50):
    colors = ["purple", "white", "blue"]
    moveToRandomLocation()
    drawSymbol(randint(5, 25), choice(colors))


hideturtle()

done()
