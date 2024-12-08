"""Turtle program to draw some pretty spiral flowers. Mostly."""

import turtle as trt


def draw_circle_spiral(radius: int | float, angle: int | float,
                       step: int, num_circles: int) -> None:
    """Draws increasing circled spirals, adding rotation each step.
    
    Parameters:
        radius int|float:
        angle int|float:
        step int:
        num_circles int:
    
    Returns: None"""

    for _ in range(num_circles):
        trt.circle(radius)
        trt.right(angle)
        radius += step


def draw_flower(petals: int, radius: int | float, angle: int | float,
                step: int) -> None:
    """Draws flower patterns using generated spiral circles.
    
    Parameters:
        petals int: Number of petals of the flower.
        radius int|float:
        angle int|float:
        step int:
    
    Returns: None"""

    for _ in range(petals):
        draw_circle_spiral(radius, angle, step, num_circles=8)
        trt.right(360 / petals)  # divide circle by number of petals for even distribution

if __name__ == "__main__":
    trt.speed(20)
    trt.clear()

    print("*" * 20)
    print("TESTING: draw_circle_spiral()")
    print("*" * 20)

    print("Testcase 1: radius=10, angle=30, step=8, num_circles=10")
    draw_circle_spiral(10, 30, 8, 10)
    trt.clear()

    print("Testcase 2: radius=5, angle=15, step=20, num_circles=20")
    draw_circle_spiral(5, 15, 20, 20)
    trt.clear()

    print("Testcase 3: radius=16, angle=5, step=5, num_circles=8")
    draw_circle_spiral(16, 6, 6, 8)
    trt.clear()

    print("*" * 20)
    print("TESTING: draw_flower()")
    print("*" * 20)

    print("\nTestcase 1: Example values")
    print("petals=10, radius=15, angle=10, step=4")
    draw_flower(10, 15, 10, 4)
    trt.clear()

    print("\nTestcase 2: petals=6, radius=20, angle=6, step=8")
    draw_flower(6, 20, 6, 8)
    trt.clear()

    print("\nTestcase 3: petals=12, radius=10, angle=15, step=10")
    draw_flower(12, 10, 15, 10)
