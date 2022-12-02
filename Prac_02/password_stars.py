def main():
    password = input("Enter Password:")
    check_length(password)
    print_password(password)


def check_length(password):
    if len(password) <= 8:
        print("Password too small")


def print_password(password):
    for i in range(len(password)):
        print("*", end="")


main()


