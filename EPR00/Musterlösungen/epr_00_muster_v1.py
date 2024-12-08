__author__ = "1234567, Tolle"

# Short program to calculate the
# division with remainder. 

# Input
a = eval(input(\
    "Bitte geben Sie den Dividend ein (natürliche Zahl): "))
b = eval(input(\
    "Bitte geben Sie Divisor (natürliche Zahl > 0): "))

# calculate quotient
quotient = a//b

# calculate remainder
remainder = a%b


# Output
print("Der Ganzzahlquotient bei der Division von ", a, " und ",b, "ist: ", quotient)
print("Der Rest bei der Division von ", a, " und ",b, "ist: ", remainder)


# Testcases (alternativ in der Doku):
# a: 32 b: 3 --> quotient 10 und remainder 2
# a: 0 b: 5 --> quotient 0 und remainder 0
# a: 5 b: 8 --> quotient 0 und remainder 5
# a: 15 b: 0 --> ZeroDivisionError: integer division or modulo by zero
