"""Treasure Hunter: A simple terminal-based treasure hunting game.

This file contains the game logic for the Treasure Hunter game.
The logic is embedded within the function treasure_hunter_game().

Driver code is found within if __name__ == "__main__" structure.
"""

__author__ = "7003725, van Reem"
__email__ = "drvanreem@stud.uni-frankfurt.de"

import game_functions as game


def get_settings() -> tuple:
    """Gets user-input for difficulty settings or custom game settings.

    Enter developer/testing mode (9999 lives) through entering "devmode" in the difficulty selection.

    :return: Game settings for the treasure_hunter_game() functionalities.
    """

    # Default settings
    difficulty = "n"
    map_size = 5
    obstacle_num = 5
    player_health = 3

    def custom_settings() -> tuple:
        """Customize option for user-controlled game settings.

        :return: Custom game settings for map_size, obstacle_num and player_health
        """

        print("How big do you want the game map to be? Standard is 5. (Minimum: 2 - Maximum: 30)")
        while True:
            try:
                custom_size = int(input("Map Size: "))
                if not 2 <= custom_size <= 30:
                    raise ValueError
            except ValueError:
                print("Invalid input! Please enter an integer between 2 and 30.")
            else:
                break

        print("How many obstacles do you want there to be? Standard is 5. (Minimum: 0 - Maximum: Map Size)")
        while True:
            try:
                custom_obstacle_num = int(input("Number of obstacles: "))
                if not 0 <= custom_obstacle_num <= custom_size*3:
                    raise ValueError
            except ValueError:
                print(f"Invalid input! Please enter an integer between 0 and {custom_size * 3}.")
            else:
                break

        print("How many lives do you want to have? Standard is 3. (Minimum: 1)")
        while True:
            try:
                custom_health = int(input("Number of lives: "))
                if 1 > custom_health:
                    raise ValueError
            except ValueError:
                print("Invalid input! Please enter an integer above 0.")
            else:
                break

        return custom_size, custom_obstacle_num, custom_health

    print("=" * 23)
    print("Which difficulty would you like to play?\n")
    print("(E)asy: 5x5 Grid, 3 obstacles, 3 lives.")
    print("(N)ormal: 5x5 Grid, 5 obstacles, 3 lives.")
    print("(H)ard: 5x5 Grid, 8 obstacles, 3 lives.")
    print("(D)eath March: 5x5 Grid, 10 obstacles, 1 life.")
    print("(C)ustom: Customise grid size, number of obstacles and number of lives.")

    while True:
        difficulty = input("Enter the (bracketed) letter to choose difficulty: ")

        match difficulty.lower():
            case "e":
                obstacle_num = 3
                break
            case "n":
                break
            case "h":
                obstacle_num = 8
                break
            case "d":
                obstacle_num = 10
                player_health = 1
                break
            case "c":
                map_size, obstacle_num, player_health = custom_settings()
                break
            case "devmode":
                player_health = 9999
                break
            case _:
                print("Invalid difficulty entered - starting game on 'normal' difficulty settings.")
                break

    return map_size, obstacle_num, player_health


def treasure_hunter_game():
    """Game logic function for the Treasure Hunter game.

    Players start at position 0,0 (top left corner of the map) and has a limited amount of lives
    to find their way to the treasure.

    :return: None
    """

    print("=" * 23)
    print("-== TREASURE HUNTER ==-")
    print("=" * 23)
    print("")

    print("Welcome to the thrill of the hunt!")
    print("In this game, your goal is to find a hidden treasure.")
    print("But beware! Obstacles make your way through this game rather perilous...")
    print("")

    # initialise starting settings for the game
    map_size, obstacle_num, player_health = get_settings()
    game_map = game.create_map(map_size)
    player_pos = game.place_element(game_map, "P", 0, 0)

    # place treasure and obstacles in the map (or rather: get their positions for the list)
    treasure_pos = game.place_element(game_map, "X")
    obstacles = [game.place_element(game_map, "O") for _ in range(obstacle_num)]
    # print(f"Obstacles: {obstacles}")  # debug

    while player_health > 0:
        print(f"Lives left: {player_health}")
        print("Current Map state:")

        game.print_map(game_map)
        direction = input("Where do you want to move? ('up', 'down', 'left' or 'right')").lower()

        # Fulfill the move (if applied)
        game_map[player_pos[0]][player_pos[1]] = "."
        new_pos = game.move_player(player_pos, direction, game_map, obstacles)

        if new_pos == player_pos:  # no movement -> wrong or illegal move
            print("You lost a life!")
            player_health -= 1

        player_pos = new_pos

        # as move_player returns the same position on error, setting game_map to player_pos
        game.place_element(game_map, "P", player_pos[0], player_pos[1])

        if player_pos == treasure_pos:
            print("Congratulations! You have found the treasure without dying!")
            return

    print("You have no more lives left!")
    print("GAME OVER")
    print(f"The treasure at {treasure_pos} will remain hidden for the next hunter...")


if __name__ == "__main__":
    treasure_hunter_game()
