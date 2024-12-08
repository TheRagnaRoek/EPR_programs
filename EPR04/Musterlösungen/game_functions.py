"""Game functions for the treasure_game.py

This module contains the following 4 functions:
1. create_map()
    - generates a 5x5 playing field as a list of lists
2. place_element()
    - places specified elements on the playing field
3. print_map()
    - prints the map in the current state into the console
4. move_player()
    - handles the player position change depending on the given direction"""

__author__ = "7003725, van Reem"
__email__ = "drvanreem@stud.uni-frankfurt.de"

import random as r

EMPTY_SPACE = "."
PLAYER = "P"
OBSTACLE = "O"
TREASURE = "X"


def create_map(size=5) -> list[list]:
    """Creates a size*size map as a list of lists (matrix)

    :param size: Size of the map (int)
    :return: Game map
    """
    game_map = [[EMPTY_SPACE for _ in range(size)] for _ in range(size)]  # list comprehension

    # alternative version using loops:
    # game_map = []
    # temp_list = []
    #
    # for _ in range(size):
    #     temp_list.append(".")
    #
    # for _ in range(size):
    #     game_map.append(temp_list)
    #
    return game_map


def place_element(game_map: list[list], element: str, x_pos=None, y_pos=None) -> tuple:
    """Places a given element randomly into the given game_map matrix.

    :param game_map: Game map (list of list/matrix)
    :param element: Element to be placed (str)
    :param x_pos: x position on the grid (row)
    :param y_pos: y position on the grid (col)
    :return:
    """

    while True:
        if x_pos is None and y_pos is None:  # assign random variables if no position is given
            x_pos = r.randint(1, 4)
            y_pos = r.randint(1, 4)
        else:
            if x_pos not in range(len(game_map)) or y_pos not in range(len(game_map)):
                print(f"Error: Invalid position coordinate (has to be within {len(game_map)})")

        if game_map[x_pos][y_pos] == EMPTY_SPACE:
            if element in {PLAYER, TREASURE}:  # only these two are always visible!
                game_map[x_pos][y_pos] = element

            return x_pos, y_pos  # position is ALWAYS returned for every element
        
        return None, None


def print_map(game_map: list[list]) -> None:
    """Prints the game map into the console.

    :param game_map: Game map (list of lists/matrix)
    :return: None
    """
    print("")
    for row in game_map:
        print(" ".join(row))
    print("")


def move_player(position: tuple[int, int], direction: str, game_map: list[list], obstacles: list) -> tuple:
    """Logic for moving the player on the game map.

    :param position: Current position of the player (tuple(int, int))
    :param direction: Direction in which the player shall be moved (str)
    :param game_map: Game map (list of lists/matrix)
    :param obstacles: List of obstacle positions (tuples)
    :return:
    """

    DIRECTIONS = {"up", "down", "left", "right"}
    x_pos, y_pos = position

    if direction not in DIRECTIONS:
        print("Invalid direction! Please enter either up, down, left or right.")
    else:
        if direction == "up" and x_pos > 0:
            x_pos -= 1
        elif direction == "down" and x_pos < len(game_map):
            x_pos += 1
        elif direction == "left" and y_pos > 0:
            y_pos -= 1
        elif direction == "right" and y_pos < len(game_map):
            y_pos += 1
        else:
            print("Can't move out of boundaries!")
            return position  # wrong input leads to returning the same position

    if (x_pos, y_pos) in obstacles:
        print("Oh no! There's an obstacle here!")
        game_map[x_pos][y_pos] = OBSTACLE  # obstacles are uncovered once they're found
        return position  # return to same position if obstacle is in the way

    return x_pos, y_pos


if __name__ == "__main__":
    # TODO: tests go here...
    print("Someone was too lazy to make tests!")
