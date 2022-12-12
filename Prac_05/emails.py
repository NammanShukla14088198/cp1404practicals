"""
CP1404 Practical
Emails
To read the name of the user from the email
"""


def main():
    name_converter = {}
    email = input("Enter your Email: ")
    while email != "":
        name = extract_name_from_email(email)
        confirm = input("Is this your name {} (Y/N)".format(name)).upper()
        if confirm == "Y":
            name_converter['{Details:}'] = name, email
            print("Hello ! {}, Welcome to CP1404...".format(name))
            print("These are you details\n {}".format(name_converter))
        elif confirm == "N":
            new_name = input("What is your Name?")
            print("Hello ! {}, Welcome to CP1404...\n Your Email is {}".format(new_name, email))
        break
    name_converter.clear()


def extract_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
