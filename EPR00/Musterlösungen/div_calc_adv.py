"""
EPR-00

Program to calculate the integer division and remainder of two numbers.
A more advanced version using try-except-blocks for error management.
"""

__author__ = "7003725, van Reem"

print("DivCalc")

# try-except block for error handling
try:
    # inputs
    a = int(input("Please input first integer (dividend): "))
    b = int(input("Please enter second integer (divisor, > 0): "))
except ValueError:
    print("Invalid input! Please make sure to enter an integer.")
else:
    # safeguard against ZeroDivisionError
    if b == 0:
        print("Invalid input for divisor: Can't divide by 0.")
    else:
        quotient = a // b
        remainder = a % b

        print(f"The quotient is {quotient}, with a remainder of {remainder}.")
