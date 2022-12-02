"""
CP1404 - Practical
Menus using looping method
"""

MENU = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter name: ")
print(MENU)
choice = input(">>>")
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice, try again!")
    print(MENU)
    choice = input(">>>")
print("Finished")