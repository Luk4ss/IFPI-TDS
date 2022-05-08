from turtle import *

speed(11)
shape("turtle")
pensize(6)
color("Blue")

for _ in range(5):
    forward(100)
    right(72)

penup()
back(300)
color("Purple")
pendown()
for _ in range(6):
    forward(100)
    right(60)


penup()
back(200)
color("Orange")
pendown()

for _ in range(360):
    forward(1)
    right(1)

done()
