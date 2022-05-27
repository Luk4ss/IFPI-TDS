
from turtle import *
from random import *


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


def moveToRandomLocation():
    penup()
    setpos(randint(-400, 400), randint(-400, 400))
    pendown()


def drawGalaxy(numberOfStars):
    starColors = ["#058396", "#0275A6", "#827E01"]
    moveToRandomLocation()
    for star in range(numberOfStars):
        penup()
        left(randint(-180, 180))
        forward(randint(5, 20))
        pendown()
        drawStar(2, choice(starColors))


def drawConstellation(numberOfStars):
    moveToRandomLocation()
    for star in range(numberOfStars - 1):
        drawStar( randint(7, 15), "white")
        pendown()
        left(randint(-90, 90))
        forward(randint(30, 70))

    drawStar(randint(7, 15), "white")



color("Red")
bgcolor("MidnightBlue")
speed(11)

for draw in range(30):
    moveToRandomLocation()
    drawStar(randint(5, 25), "white")


for galaxy in range(3):
    drawGalaxy(40)

for constellation in range(2):
    drawConstellation(randint(4, 7))

hideturtle()
done()


"""



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


"""

