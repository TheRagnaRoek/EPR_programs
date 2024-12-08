"""
EPR-U01-1
A simple converter of Celsius to Fahrenheit.
"""

__author__ = "7003725, Dennis van Reem"

# absolute zero - no lower temperature possible
LOWEST_TEMP_CELSIUS: float = -273.15

# input
temp_c = float(input("Enter a temperature in degrees Celsius (minimum is -273.15): "))

# logic to determine correct temperature input range
if temp_c < LOWEST_TEMP_CELSIUS:
    print("Input is below lowest possible temperature.")
else:
    temp_fahr: float = temp_c * 9/5 + 32
    print(f"{temp_c} °C converted to Fahrenheit is {temp_fahr} °F.")
