"""
CP1404 Practical

1.Change the first element of numbers to "ten" (the string, not the number 10)
2.Change the last element of numbers to 1
3.Print all the elements from numbers except the first two (slice)
4.Print whether 9 is an element of numbers
"""
# copied the list from github
numbers = [3, 1, 4, 1, 5, 9, 2]

#
numbers[0] = "ten"

# to replace the last number in the list with 1
numbers[-1] = 1

# to print all the elements after the first two
x = numbers[2:]
print(x)

# to check whether 9 is in the list numbers
y = 9 in numbers
print(y)









