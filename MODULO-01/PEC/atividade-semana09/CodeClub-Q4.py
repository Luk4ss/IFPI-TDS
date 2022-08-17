from turtle import *

speed(8)
shape("turtle")
color("blue")
pensize(7)

lados = 8

angulo = 360 / lados

for _ in range(lados):
    forward(100)
    right(angulo)

done()
