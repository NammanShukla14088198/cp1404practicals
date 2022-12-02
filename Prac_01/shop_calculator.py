"""
CP1404 - Practical
Shop Calculator
Allows user to input the number of items and price for each individually
display the total price of the items

Condition:
if the total price is over 100$ then 10% discount is applied (before the amount is displayed to the user)
"""
total = 0
no_of_items = int(input("Number of Items: "))
if no_of_items < 0:
    print("Invalid number!")
for i in range(no_of_items):
    price = float(input("Price of item: "))
    total += price
if total > 100:
    total *= 0.9
print("Total price for ", no_of_items, " items is $", round(total), sep='')
