"""
CP1404 Practical
Hex Colors
Finding the code for the color
"""

CODE_OF_COLOR = {"asparagus": "#0048ba", "acid green": "#b0bf1a", "matcha green": "#69bf64", "bright green": "#66ff00",
                 "brunswick green": "#1b4d3e", "cadmium green": "#006b3c"}

COLOR_OPTIONS = " Asparagus\n Acid Green\n Matcha Green\n Bright Green\n Brunswick Green\n Cadmium Green"
print(COLOR_OPTIONS)

userInput = input("Choose a color from the color bar above(^) : ").lower()
while userInput != "":
    if userInput in CODE_OF_COLOR:
        print("{} has the code: {}".format(userInput, CODE_OF_COLOR[userInput]))
    else:
        print("Invalid choice ! try again...")
    userInput = input("Choose a color from the color bar above(^) : ").lower()


