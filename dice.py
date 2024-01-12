import turtle
import random


def roll_die():
    return random.randint(1, 6)

def dot(value, x, y):
    dot_positions = []
    if value == 1:
        dot_positions = [
            (x + 25, y - 25)
        ]
    elif value == 2:
        dot_positions = [
            (x + 12.5, y - 37.5),
            (x + 37.5, y - 12.5)
        ]
    elif value == 3:
        dot_positions = [
            (x + 25, y - 25),
            (x + 12.5, y - 37.5),
            (x + 37.5, y - 12.5)
        ]
    elif value == 4:
        dot_positions = [
            (x + 12.5, y - 37.5),
            (x + 12.5, y - 12.5),
            (x + 37.5, y - 12.5),
            (x + 37.5, y - 37.5)
        ]
    elif value == 5:
        dot_positions = [
            (x + 12.5, y - 37.5),
            (x + 12.5, y - 12.5),
            (x + 37.5, y - 12.5),
            (x + 37.5, y - 37.5),
            (x + 25, y - 25)
        ]
    elif value == 6:
        dot_positions = [
            (x + 12.5, y - 37.5),
            (x + 12.5, y - 12.5),
            (x + 37.5, y - 12.5),
            (x + 37.5, y - 37.5),
            (x + 12.5, y - 25),
            (x + 37.5, y - 25),
        ]
    else:
        raise ValueError
        
    return dot_positions        

def draw_die(value, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.fillcolor("white")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()

    turtle.penup()
    dot_positions = dot(value, x, y)
    for d in dot_positions:
        turtle.goto(d)
        turtle.dot(8, "black")

def display_dice_roll():
    turtle.speed(0)

    die1 = roll_die()
    die2 = roll_die()

    draw_die(die1, -200, 200)
    draw_die(die2, -125, 200)
    
    turtle.hideturtle()


def play():
    while True:
        display_dice_roll()
        inp = turtle.textinput("Next Roll", "Press enter to roll again, or type Q to quit:")
        if inp and inp.lower() == 'q':
            turtle.bye()
            break
