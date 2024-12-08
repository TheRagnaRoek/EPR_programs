"""
EPR-U01-1
A more advanced converter of Celsius to Fahrenheit.

Includes a converter function and a function loop for input safety.
"""

__author__ = "7003725, van Reem"


LOWEST_TEMP_CELSIUS: float = -273.15

def celsius_to_fahrenheit(temp: float) -> float:
    """Converts celsius temperature to fahrenheit"""

    temp_fahr: float = temp * 9/5 + 32
    return temp_fahr


while True:  # input loop
    try:
        temp_c = float(input("Enter a temperature in degrees Celsius (minimum is -273.15): "))
    except ValueError:
        print("Input was invalid - please enter an integer or float (using a dot).")
    else:
        if temp_c < LOWEST_TEMP_CELSIUS:
            print("Input is below lowest possible temperature.")
        else: break

conv_temp: float = celsius_to_fahrenheit(temp_c)
print(f"{temp_c} °C converted to Fahrenheit is {conv_temp} °F.")
