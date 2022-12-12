"""
CP1404 Practical
Hex Colors
Finding the code for the color
"""

CODE_OF_COLOR = {"asparagus": "#0048ba", "acid green": "#b0bf1a", "matcha green": "#69bf64", "bright green": "#66ff00",
                 "brunswick green": "#1b4d3e", "cadmium green": "#006b3c", "caribbean green": "	#00cc99",
                 "camouflage green": "#78866b", "castleton green": "#00563f", "celadon": "#ace1af"}
print("Hex Color Green: Choose a color to find it's hex code !")
COLOR_OPTIONS = " Asparagus\n Acid Green\n Matcha Green\n Bright Green\n Brunswick Green\n Cadmium Green\n Caribbean " \
                "Green\n Camouflage Green\n Castleton Green\n Celadon "
print(COLOR_OPTIONS)

userInput = input("Your Choice: ").lower()
while userInput != "":
    if userInput in CODE_OF_COLOR:
        print("{} has the code: {}".format(userInput, CODE_OF_COLOR[userInput]))
    else:
        print("Invalid choice ! try again...")
    userInput = input("Choose a color from the color bar above(^) : ").lower()


