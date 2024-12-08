"""
This program contains two mathematical equations programmed in Python:
1. Fibonacci-Sequence to the n-th number.
2. Sum of k! over (k+1)
"""


__author__ = "van Reem, 7003725"
__email__ = "drvanreem@stud.uni-frankfurt.de"


def fibonacci(num: int) -> list:
    """Calculates the fibonacci sequence until the given fibonacci number."""

    fib_sequence: list = []

    if num == 1:  # "base case"
        fib_sequence = [1]
    else:
        fib_sequence = [1, 1]
        for _ in range(num-2):  # num-2 because we already did the first 2!
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence


def sum_equation(num: int) -> float:
    """Calculates the formula:
    Sum n over k=1 of all k!/k+1"""

    def factorial(n: int) -> int:
        """Simple factorial calculation function"""

        fact = 1
        for i in range(2, n+1):
            fact *= i  # fact = fact * i
        return fact

    result: float = 0.0

    for i in range(1, num+1):
        result += factorial(i) / (i + 1)
    return result


if __name__ == "__main__":  # driver function
    # options input from user
    choice = input("Please enter 'F' for Fibonacci, 'K' for the k-sum-equation-thingy or anything else to exit: ")
    
    match choice.lower():
        case "f":  # Fibonacci-Calculator
            while True:
                try:
                    fib_input = int(input("Please enter a positive integer for the Fibonacci-sequence: "))
                except ValueError:
                    print("Invalid input - not an integer.\n")
                else:
                    if fib_input < 0:
                        print("Invalid input - not a positive integer.")
                    else:
                        print(f"Fibonacci sequence up to the {fib_input}th number:")
                        print(fibonacci(fib_input))
                        break

        case "k":  # K-Sum-Thingy
            while True:
                try:   
                    k_input = int(input("Please enter a positive integer: "))
                except ValueError:
                    print("Invalid input - not an integer.\n")
                else:
                    if k_input < 0:
                        print("Invalid input - not a positive integer.")
                    else:
                        print(f"The sum of all k!/(k+1) from 1 to {k_input} is:")
                        print(sum_equation(k_input))
                        break

        case _:
            print("Exiting program. Cya!")
