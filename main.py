""" 
    Josh Cohn
    January 2024    
"""

from hex import *
from dice import *

def run():
    # Creat board
    create_board()
    
    # Check to see if board works
    #     DOES NOT WORK YET
    board_check()
    
    # Turtle draws the board
    turtle_board()
    
    # Start the dice rolling process
    play()
    turtle.done()

def main():
    run()

if __name__ == '__main__':
    main()