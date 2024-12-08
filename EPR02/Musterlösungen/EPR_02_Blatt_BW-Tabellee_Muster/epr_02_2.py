
__author__ = "7592047, Khauto"
__email__ = "khauto@em.uni-frankfurt.de"



# inputs from user
tree_height = int(input("Gib die Höhe des Baums ein: "))
trunk_height = int(input("Gib die Höhe des Stamms ein: "))

"""
# Für die Doku ist hier wichtig zu erklären, wie sie mit den Indizien gearbeitet haben.
# Und wie sie es geschafft habe, einen Baum zu zeichnen, wie viele Spaces sie gelassen haben
# und wie es entschieden wurde.
"""

# first loop for tree height (rows)
for row in range(tree_height):

    # calculate how many spaces
    spaces_num = tree_height - row - 1 
    # loop for the spaces
    for space in range(spaces_num):
        print(" ", end="")
    # calculate how many stars for each row
    stars_num = row * 2 + 1
    # loop for the stars
    for star in range(stars_num):
        print("*", end="")
    
    print()


# loop for the trunk
for _ in range(trunk_height):  
    for space in range(tree_height - 2):
        print(" ", end="")
    print("|||")

