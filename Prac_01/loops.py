"""
CP1404- Practical
Variation in Loops
"""
# odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# A) counting in 10s from 10 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# B) counting down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# C) printing stars determined with user input

no_of_stars = int(input("How many number of stars would you like ? : "))
if no_of_stars < 0:
    print("Invalid Input")
for i in range(no_of_stars):
    print('*', end=' ')
print()

# D) printing stars in increments

for i in range(1, no_of_stars + 1):
    print('*' * i)
print()