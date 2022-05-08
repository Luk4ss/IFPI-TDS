from turtle import *

shape("turtle")
pensize(6)
speed(6)
color("Orange")

for _ in range(0, 4):
    forward(100)
    right(90)

color("Purple")
penup()
back(200)
pendown()

left(60)
for _ in range(0, 3):
    forward(100)
    right(60)
    forward(100)
    right(120)
    forward(100)
    right(60)
    forward(100)

color("Blue")
penup()
forward(200)
pendown()

for _ in range(0, 3):
    forward(100)
    right(120)


done()


