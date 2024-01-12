""" 
    Josh Cohn
    January 2024    
"""

import random
import turtle

from dice import *

# Lists attributes for the board, and the board itself
num = []
res = []
board = []

# Size of the board
SIZE = 19

# Colors that are associated with each resource
resource_colors = {
    "wo": "green",
    "br": "#FFC0CB",
    "wh": "yellow",
    "sh": "lightgreen",
    "mo": "gray",
    "de": "white"
}

# Hex class 
# 
# A hex is a tile on the board. It is 
# assigned a resource, and a random number 
# 2 - 12 (excluding 7).
class Hex:
    
    __slots__ = ['resource', 'number']
    
    def __init__ (self, resource, number):
        self.resource = resource
        self.number = number
        
    def __str__(self):
        return f"{self.number} {self.resource}"    
    
    def get_num(self):
        return self.number
    
    def get_res(self):
        return self.resource

# Filling out lists from our text files
def set_up():
    with open('hex_docs/numbers.txt', 'r') as file:
        for line in file:
            num.append(line.strip())
    with open('hex_docs/resources.txt', 'r') as file:
        for line in file:
            res.append(line.strip())
    
    # Shuffling so everything is random
    random.shuffle(num)
    random.shuffle(res)

# adding resource hexes to the board list
def create_board():
    set_up()
    for i in range(len(num)):
        board.append(Hex(res[i], num[i]))
    board.append(Hex("de", 0))
    random.shuffle(board)

# Command line printing of the board
def print_board():
    rows = [
        [0, 1, 2],
        [3, 4, 5, 6],
        [7, 8, 9, 10, 11],
        [12, 13, 14, 15],
        [16, 17, 18]
    ]

    longest_row = max(len(row) for row in rows)
    
    for row in rows:
        num_spaces = longest_row - len(row)
        print("  " * num_spaces, end="")
        for index in row:
            if index < len(board):
                print(board[index], end="\t\t")
        print()



#############################################################
##          Everything in this section is turtle           ##
#############################################################

# Drawing each hex
def draw_hexagon(side_length, item):
    turtle.begin_fill()
    turtle.fillcolor(resource_colors.get(item.resource, "white"))  # Get color from dictionary, default to white
    turtle.left(30)
    for _ in range(6):
        turtle.pendown()
        turtle.forward(side_length)
        turtle.left(60)
        turtle.penup()
    turtle.end_fill()
    turtle.right(30)
    turtle.left(90)
    turtle.forward(side_length * .75)
    turtle.write(item, align="center", font=("Arial", 16, "normal"))
    turtle.backward(side_length * .75)
    turtle.right(90)

    
    
# Drawing a row of hexagons of length (L)
def draw_row_of_hexagons(L):
    hex_size = 50
    for _ in range(L):
        draw_hexagon(hex_size, board.pop(0))
        turtle.forward(hex_size * 1.75)

# Reset turtle for new row that increases in size from previous
def new_row(hex_size, start):
    turtle.goto(start)
    turtle.right(90)
    turtle.forward(hex_size*1.6)
    turtle.right(90)
    turtle.forward(hex_size*.85)
    turtle.left(180)
    return turtle.position()

# Reset turtle for new row that decreases in size from previous
def new_row_op(hex_size, start):
    turtle.goto(start)
    turtle.right(90)
    turtle.forward(hex_size*1.6)
    turtle.left(90)
    turtle.forward(hex_size*.85)
    return turtle.position()

# calls above helper functions to create the board in turtle
def turtle_board():
    turtle.bgcolor("lightblue")
    hex_size = 50  
    start = -2 * hex_size, 0
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-2 * hex_size, 0)
    turtle.pendown()
    
    
    draw_row_of_hexagons(3)
    start = new_row(hex_size, start)
    draw_row_of_hexagons(4)
    start = new_row(hex_size, start)
    draw_row_of_hexagons(5)
    start = new_row_op(hex_size, start)
    draw_row_of_hexagons(4)
    start = new_row_op(hex_size, start)
    draw_row_of_hexagons(3)
    

#############################################################



# Needs to be fixed
# We want to check to make sure there are no illegal spots on the board.
# 
#   An illegal spot is any number adjacent to
#   itself. For example, multiple 3's in hexes that
#   are touching each other on the board. Also, a 6
#   is not allowed to be adjacent to an 8. 
def board_check():
    while True:
        random.shuffle(board)
        for i in range(len(board) - 1):
            if board[i].get_num() == board[i + 1].get_num():
                continue
        break
