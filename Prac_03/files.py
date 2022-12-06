"""
CP1404 Practical
Files.py
1. Write code that asks the user for their name,
then opens a file called "name.txt" and writes that name to it. Remember to close your file.

2. (In the same file, but as if it were a separate program) Write code that opens "name.txt" and reads the name
(as above) then prints,"Your name is Bob" (or whatever the name is in the file).

3. Create a text file called numbers.txt and save it in your prac directory. Put the following three numbers on separate
lines in the file and save it:
17,42,400
Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result,
which should be... 59.

4. Now write a fourth block of code that prints the total for all lines in numbers.txt
or a file with any number of numbers
"""

# Answer 1, takes the user input and then writes in names.txt
userInput = input("Enter your name: ")
f = open("name.txt", "w")
if len(userInput) == 0:
    print("invalid name")
    userInput = input("Enter your name: ")
else:
    f.write(userInput)
    f.close()

# Answer 2, read the previous file and prints the name
f = open("name.txt", "r")
print("Your name is {}".format(f.read()))

# Answer 3, open the file, add the first 2 lines
f = open("numbers.txt", "r")
number_1 = int(f.readline())
number_2 = int(f.readline())
print(number_1 + number_2)

# Answer 4, open the file, declare a variable for the sum and using a for loop to add all the lines
f = open("numbers.txt", "r")
total_of_numbers = 0
for n in f:
    number = int(n)
    total_of_numbers += number
f.close()
print(total_of_numbers)















