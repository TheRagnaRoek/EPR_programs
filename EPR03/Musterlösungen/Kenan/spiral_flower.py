"""
spiral_flower.py contains two functions to draw a spiral flower with their testcases.
"""
__author__ = "7592047, Khauto"
__email__ = "khauto@em.uni-frankfurt.de"


import turtle

def draw_circle_spiral(radius=20, angle=15, step=5, num_circles=10):
    """
    Draws a spiral of circles, gradually increasing the radius and rotating.

    Parameters:
        radius (int): Initial radius of each circle in the spiral.
        angle (int): Angle to rotate the turtle after each circle.
        step (int): Increment for the radius after each circle to create the spiral effect.
        num_circles (int): Number of circles to draw in the spiral.

    Returns:
        None
    """
    for _ in range(num_circles):
        turtle.circle(radius)
        turtle.right(angle)  # Rotate by the specified angle
        radius += step       # Increase radius for the next circle


def draw_flower(petals=6, radius=20, angle=15, step=5):
    """
    Draws a flower shape using multiple spiral patterns, each representing a petal.

    Parameters:
        petals (int): Number of petals (spirals) to draw.
        radius (int): Initial radius of each circle in a petal.
        angle (int): Angle to rotate the turtle within each petal spiral.
        step (int): Increment for the radius within each petal spiral.

    Returns:
        None
    """
    for _ in range(petals):
        draw_circle_spiral(radius, angle, step, num_circles=10)  # Each petal is a spiral of 10 circles
        turtle.right(360 / petals)  # Rotate to place the next petal evenly around the center


if __name__ == "__main__":
    turtle.speed(0)  # Fastest drawing speed for testing
    turtle.color("blue")

    print("Running test cases for draw_circle_spiral and draw_flower...")

    print("Test Case 1: draw_circle_spiral() with default parameters")
    draw_circle_spiral()
    turtle.clear()

    print("Test Case 2: draw_circle_spiral(radius=30, angle=10, step=2, num_circles=15)")
    draw_circle_spiral(radius=30, angle=10, step=2, num_circles=15)
    turtle.clear()

    print("Test Case 3: draw_flower(petals=8, radius=25, angle=20, step=3)")
    draw_flower(petals=8, radius=25, angle=20, step=3)
    turtle.clear()

    print("Test Case 4: draw_flower(petals=10, radius=15, angle=10, step=4)")
    draw_flower(petals=10, radius=15, angle=10, step=4)
    turtle.clear()

    print("Test Case 5: draw_flower(petals=12, radius=10, angle=15, step=10)")
    draw_flower(petals=12, radius=10, angle=15, step=10)
    turtle.clear()

    turtle.done()

