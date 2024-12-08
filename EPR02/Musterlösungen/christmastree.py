"""
This program takes user input to determine the height of a tree, and
prints it into the terminal in a proper way.

Created with the use of ChatGPT.
"""

__author__ = "van Reem, 7003725"
__email__ = "drvanreem@stud.uni-frankfurt.de"

def christmas_tree(leaves_height, trunk_height):
    """Holly Jolly Christmas!"""

    # printing the leaves
    for i in range(leaves_height):
        # width increases per level
        spaces = ' ' * (leaves_height - i - 1)  # whitespaces for central alignment
        stars = '*' * (2 * i + 1)
        print(spaces + stars)
    
    # printing the trunk
    trunk_width = leaves_height // 2  # adjust the trunk width to match tree heighth
    trunk_spaces = ' ' * (leaves_height - trunk_width // 2 - 1)

    for _ in range(trunk_height):  # trunk width remains the same
        print(trunk_spaces + '|' * trunk_width)

if __name__ == "__main__":
    tree_height_input = int(input("Enter tree height: "))
    trunk_height_input = int(input("Enter trunk height: "))
    christmas_tree(tree_height_input, trunk_height_input)
