import turtle as t
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def move_to_start():
    turn_around()
    for _ in range(17):
        move_forward()

    turn_left()
    for _ in range(15):
        move_forward()
    turn_left()


def move_forward():
    turtle.forward(20)


def fill_line():
    for _ in range(34):
        turtle.dot(12, random_color())
        move_forward()
    turtle.dot(12, random_color())


def turn_left():
    turtle.left(90)


def turn_right():
    turtle.right(90)


def turn_around():
    turtle.left(180)


turtle = t.Turtle()
turtle.hideturtle()
turtle.penup()
t.colormode(255)
turtle.speed('fastest')

move_to_start()

for i in range(16):
    fill_line()
    turn_left()
    move_forward()
    turn_left()
    fill_line()
    turn_right()
    move_forward()
    turn_right()


screen = t.Screen()
screen.exitonclick()
