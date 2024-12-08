"""

"""

__author__ = "7592047, Khauto"
__email__ = "khauto@em.uni-frankfurt.de"

import random

def create_map():
    """
    Creates a 5x5 grid as the game map.
    Each cell is initialized with a "." to represent an empty space.
    
    Returns:
        list: A 5x5 list of lists representing the grid.
    """
    return [["." for _ in range(5)] for _ in range(5)]

def place_element(game_map, element):
    """
    Places a specific element (e.g., treasure or obstacle) at a random empty position on the map.
    Obstacles would stay hidden until running into them.
    
    Args:
        game_map (list): The 2D grid representing the game map.
        element (str): The element to be placed, such as "X" for the treasure or "O" for obstacles.
    
    Returns:
        tuple: The coordinates (x, y) where the element was placed.
    """
    while True:
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        if game_map[x][y] == ".":  # Ensure the position is empty
            if element == "O":
                return (x, y)
            game_map[x][y] = element
            return (x, y)

def print_map(game_map):
    """
    Prints the current state of the game map to the console.
    Each row of the map is displayed on a new line, with cells separated by spaces.
    
    Args:
        game_map (list): The 2D grid representing the game map.
    """
    for row in game_map:
        print(" ".join(row))
    print()

def move_player(position, direction, game_map, obstacles):
    """
    Moves the player in the specified direction, if the move is valid.
    Valid moves stay within the boundaries of the map and avoid obstacles.
    
    Args:
        position (tuple): The current coordinates of the player (x, y).
        direction (str): The direction of movement ("up", "down", "left", "right").
        game_map (list): The 2D grid representing the game map.
        obstacles (list): The list of obstacle positions.
    
    Returns:
        tuple: The new coordinates (x, y) of the player after the move.
    """
    x, y = position
    if direction == "up" and x > 0:
        x -= 1
    elif direction == "down" and x < 4:
        x += 1
    elif direction == "left" and y > 0:
        y -= 1
    elif direction == "right" and y < 4:
        y += 1
    else:
        print("Invalid move! You can't go outside the map boundaries.")
        return position  # Return the current position if the move is invalid

    if game_map[x][y] == "O":
        print("You can't move onto an obstacle!")
        return position  # Return the current position if an obstacle is in the way
    if (x, y) in obstacles:
        print("You have stumpled onto an obstacle! you lost one move and you can't move there!")
        obstacles.remove((x, y))
        game_map[x][y] = "O"  # Return the current position if an obstacle is in the way
        return position
    return (x, y)

def treasure_hunter_game():
    """
    Main function to run the Treasure Hunter game.
    The player starts at the top-left corner of a 5x5 grid and has 10 moves to find the treasure.
    The game includes obstacles that block the player's path.
    """
    # Create the game map and initialize the player position
    game_map = create_map()
    player_position = (0, 0)
    game_map[player_position[0]][player_position[1]] = "P"

    # Place the treasure and obstacles on the map
    treasure_position = place_element(game_map, "X")
    obstacles = [place_element(game_map, "O") for _ in range(5)]

    # Set the move limit
    move_limit = 10


    print("Welcome to the Treasure Hunter Game!")
    print("Your goal is to find the treasure (X) within 10 moves.")
    print("Be careful of obstacles (O) blocking your path.")
    print("The current game map:")
    print_map(game_map)

    while move_limit > 0:
        print(f"Remaining moves: {move_limit}")
        direction = input("Where do you want to move? ('up', 'down', 'left', 'right'): ").lower()

        if direction not in ["up", "down", "left", "right"]:
            print("Invalid input! Please choose 'up', 'down', 'left', or 'right'.")
            continue

        # Clear the player's current position on the map
        game_map[player_position[0]][player_position[1]] = "."

        new_position = move_player(player_position, direction, game_map, obstacles)
        player_position = new_position
        # Mark the new player position on the map
        game_map[player_position[0]][player_position[1]] = "P"

        print_map(game_map)


        if player_position == treasure_position:
            print("Congratulations! You found the treasure!")
            return


        move_limit -= 1


    print("You ran out of moves! Game over.")
    print(f"The treasure was hidden at {treasure_position}.")

treasure_hunter_game()
