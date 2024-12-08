"""
Calculate the price of wares, including potential discounts for mass orders.

Input number of items and price per item, get total cost including discount.
"""

__author__ = "7003725, van Reem"

# Discounts
# > 5 units - 5%
# > 10 units - 7%
# > 100 units - 15%

print("<<< PythonMarket >>>")
price_per_item: float = float(input("Price per item: "))
number_items: int = int(input("Number of items: "))

# bigger discounts get checked first
if number_items > 100:
    print("You get a discount of 15%!")
    total = number_items * price_per_item * 0.85
elif number_items > 10:
    print("You get a discount of 7%!")
    total = number_items * price_per_item * 0.93
elif number_items > 5:
    print("You get a discount of 5%!")
    total = number_items * price_per_item * 0.95
else:
    print("No discounts applied.")
    total = number_items * price_per_item

print(f"Your total price is {round(total, 2)}EUR, rounded to cents.")
