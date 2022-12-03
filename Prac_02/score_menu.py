"""
CP1404 Practical
Build a menu
(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit
"""

MENU = " (G)et a valid score\n (P)rint result\n (S)how stars\n (Q)uit"


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            get_score()
            print(MENU)
        elif choice == "P":
            print_score(result)
            print(MENU)
        elif choice == "S":
            show_stars(result)
            print(MENU)
        else:
            print("Invalid option")
            print(MENU)
        choice = input(">>> ").upper()
    print("farewell")


def get_score():
    result = int(input("Enter Score: "))
    if result < 0 or result > 100:
        print("Invalid score")
        print(MENU)
    else:
        print("Your score is {} which is valid !".format(result))
    return result


def print_score(result):
    from score import check_score
    check_score(result)


def show_stars(result):
    for i in range(result):
        print("*", end="")


main()
