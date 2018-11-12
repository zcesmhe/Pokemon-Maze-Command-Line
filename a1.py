#!/usr/bin/env python3
###################################################################
#
#   CSSE1001/7030 - Assignment 1
#
#   Student Username: s4442951
#
#   Student Name: Mounir Hedna
#
###################################################################

###################################################################
#
# The following is support code. DO NOT CHANGE.

from a1_support import *

# End of support code
################################################################

# Write your code here

def interact():
    # Add your code for interact here
    """Interact will continuously loop until and ask the user for input until the game is over"""

    COMMANDS = "n s e w r b p q ?"
    """To add new commands, add the new character to the commands string making
    sure there is a space in between each character"""
    
    file = input("Maze File: ").strip()
    maze = load_maze(file)
    current_position = START_POSITION
    moves = []

    game_over = False
    while(not game_over):
        
        print()
        print_maze(maze, current_position)
        print()

        try:
            command = input("Command: ").strip()
        except EOFError:
            pass
            
        legal_moves = get_legal_directions(maze, current_position)
        
        if command not in COMMANDS or command == "":
            print("Invalid command: " + command)

        elif command in legal_moves:
            pos = move(maze, current_position, command)
            if pos[1] in BAD_POKEMON:
                print(LOSE_TEXT.format(POKEMON.get(pos[1])))
                game_over = True
            elif pos[1] in GOOD_POKEMON:
                print(WIN_TEXT.format(POKEMON.get(pos[1])))
                game_over = True

            else:
                moves.append(current_position)
                current_position = pos[0]

        elif command == "r":
            current_position = START_POSITION
            moves = []

        elif command == "b":
            if len(moves) == 0:
                print("You cannot go back from the beginning.")

            else:
                current_position = moves.pop()

        elif command == "?":
            print(HELP_TEXT)

        elif command == "p":
            p = ""
            count = 0
            
            for m in legal_moves:
                if count == len(legal_moves)-1:
                    p += m
                else:
                    p += m + ", "
                    count += 1
            
            print("Possible directions: " + p)

        elif command == "q":
            try:
                quit_game = input("Are you sure you want to quit? [y] or n: ").strip()

            except EOFError:
                pass
                
            if quit_game == "y":
                game_over = True

        else:
            print("You can't go in that direction.")


def get_position_in_direction(position, direction):
    """Takes a position (coordinate) and a direction from "n,e,s,w" and returns the
       new coordinate.

       get_position_in_direction((int, int), str) -> (int, int)
       """
    dP = DIRECTION_DELTAS.get(direction)
    x = position[1] + dP[1]
    y = position[0] + dP[0]

    return (y, x)

def print_maze(maze, position):
    """Takes a maze and a position (coordinate) and prints the maze with position marked
    with an 'A'.

    print_maze(str, (int, int)) -> None
    """
    rows = maze.split("\n")
    new_row = list(rows[position[0]])
    new_row[position[1]] = PLAYER
    rows[position[0]] = "".join(new_row)

    for row in rows:
        print(row)

def move(maze, position, direction):
    """Takes in a maze, a position and a direction. Returns the position after moving
       in the given direction and the value at that position.

       move(str, (int, int), str) -> ((int, int), str)
       """
    position2 = get_position_in_direction(position, direction)
    rows = maze.split("\n")
    row = rows[position2[0]]
    value = row[position2[1]]

    if value == WALL:
        return (position, WALL)
    else:
        return (position2, value)

def get_legal_directions(maze, position):
     """Takes a maze and a position coordinate and returns all legal directions
        you are able to move in.

        get_legal_directions(str, (int, int)) -> list<str>
        """
     available_directions = []
     for d in DIRECTIONS:
         m = move(maze, position, d)
         if m[1] != WALL:
             available_directions += d
     return available_directions

##################################################
# !!!!!! Do not change (or add to) the code below !!!!!
# 
# This code will run the interact function if
# you use Run -> Run Module  (F5)
# Because of this we have supplied a "stub" definition
# for interact above so that you won't get an undefined
# error when you are writing and testing your other functions.
# When you are ready please change the definition of interact above.
###################################################

if __name__ == '__main__':
    interact()
