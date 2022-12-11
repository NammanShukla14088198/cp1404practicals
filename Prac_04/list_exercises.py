"""
CP1404 Practical
List-exercises
"""

numbers = []
for i in range(5):
    userInput = int(input("Enter 5 numbers: "))
    numbers.append(userInput)
print("You entered {} as your first number".format(numbers[0]))
print("You entered {} as your last number".format(numbers[-1]))
print("The lowest number you entered was {}".format(min(numbers)))
print("the highest number you entered was {}".format(max(numbers)))
print("the average of the numbers you entered was {}".format(sum(numbers)/len(numbers)))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

input_username = input("Enter your username: ")

if input_username in usernames:
    print("Access Granted!")
else:
    print("Access Denied")

