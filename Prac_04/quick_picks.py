"""
CP1404 Practical
Quick Picks (Using Random)
"""

import random

NUMBER_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45

try:
    userInput = int(input("How many quick picks: "))
except ValueError:
    print("Invalid input! try again...")
    userInput = int(input("How many quick picks: "))

while userInput <= 0:
    print("Invalid number! try again...")
    userInput = int(input("How many quick picks: "))

for i in range(userInput):
    quick_picks = []
    for x in range(NUMBER_PER_LINE):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in quick_picks:
            number = random.randint(MINIMUM, MAXIMUM)
        quick_picks.append(number)
    quick_picks.sort()
    print(" ".join(f"{number:2}" for number in quick_picks))




