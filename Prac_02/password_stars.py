password = input("Enter Password:")
if len(password) <= 8:
    print("Password too small")
else:
    for i in range(len(password)):
        print("*", end="")

        