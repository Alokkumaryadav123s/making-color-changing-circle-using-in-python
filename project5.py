from turtle import *

speed(0)
bgcolor("black")
colors = ["orange", "white"]  # renamed from color → colors
hideturtle()
for i in range(122):
    goto(0, 0)
    color(colors[i % 2])  # use the turtle color() function
    forward(130)
    left(3)
    circle(40)
    forward(130)
    right(180)

done()