"""
EPR-00

Program to calculate the integer division and remainder of two numbers.
"""

__author__ = "7003725, van Reem"

print("DivCalc")

# inputs
a = int(input("Please input first integer (dividend): "))
b = int(input("Please enter second integer (divisor, > 0): "))

# safeguard against ZeroDivisionError
if b == 0:
    print("Error: Can't divide by zero.")
else:
    print(f"Calculating: {a} / {b}")

    quotient = a // b
    remainder = a % b

    print(f"The integer division is {quotient}, with a remainder of {remainder}.")
