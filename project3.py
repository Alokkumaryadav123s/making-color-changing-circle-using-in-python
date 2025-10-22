import turtle
import time
import random

try:
    from pyfiglet import figlet_format
    print(figlet_format("wishing you a bright and joyful diwali!", font="slant"))
except:
    print("wishing you a bright and joyful diwali!".center(60, "="))


# Set up turtle screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Happy Diwali - Turtle Animation")

# Create turtle for drawing diya
diya = turtle.Turtle()
diya.speed(8)
diya.pensize(3)
colors = ["red", "orange", "yellow", "white", "gold"]

def draw_diya():
    diya.penup()
    diya.goto(0, -100)
    diya.pendown()
    diya.color("orange")
    diya.begin_fill()
    diya.circle(100)
    diya.end_fill()

    # Flame
    diya.penup()
    diya.goto(0, 20)
    diya.color("yellow")
    diya.begin_fill()
    diya.circle(20)
    diya.end_fill()

    diya.penup()

def burst_firework(x, y):
    fire = turtle.Turtle()
    fire.hideturtle()
    fire.speed(0)
    fire.color(random.choice(colors))
    fire.penup()
    fire.goto(x, y)
    fire.pendown()
    for _ in range(36):
        fire.forward(100)
        fire.backward(100)
        fire.left(10)
    fire.clear()

def show_fireworks():
    for _ in range(5):
        x = random.randint(-200, 200)
        y = random.randint(0, 200)
        burst_firework(x, y)
        time.sleep(0.5)

# Draw diya
draw_diya()

# Show fireworks
show_fireworks()

# Final message
msg = turtle.Turtle()
msg.hideturtle()
msg.penup()
msg.color("white")
msg.goto(0, -200)
msg.write("Wishing You a Bright and Joyful Diwali!", align="center", font=("Arial", 16, "bold"))

# Keep the window open
turtle.done()