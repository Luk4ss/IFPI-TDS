from turtle import *

speed(11)
shape("turtle")
color("blue")
pensize(7)

for _ in range(6):
    forward(100)
    right(60)
    back(50)

color("Purple")
penup()
forward(200)
pendown()

for _ in range(25):
    forward(100)
    left(82)

done()
