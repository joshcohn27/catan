import turtle
import random

def roll_die():
    return random.randint(1, 6)

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
    dot_positions = [
        (x + 15, y - 35),  # Top-left
        (x + 35, y - 35),  # Top-right
        (x + 15, y - 15),  # Bottom-left
        (x + 35, y - 15),  # Bottom-right
        (x + 25, y - 25),  # Center
        (x + 25, y - 45),  # Top-center
    ]

    for i in range(value):
        turtle.goto(dot_positions[i])
        turtle.dot(8, "black")

def display_dice_roll():
    turtle.speed(0)

    die1 = roll_die()
    die2 = roll_die()

    draw_die(die1, -200, 200)
    draw_die(die2, -125, 200)
    
    # turtle.color("black")
    # turtle.goto(0, 200)
    # turtle.write(die1+die2, align="center", font=("Arial", 16, "normal"))
    # turtle.penup()
    
    turtle.hideturtle()


def play():
    while True:
        display_dice_roll()
        inp = turtle.textinput("Next Roll", "Press enter to roll again, or type Q to quit:")
        if inp and inp.lower() == 'q':
            turtle.bye()
            break
