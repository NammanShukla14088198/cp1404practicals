import random

# the random module is helping to generate pseudo-random numbers in this line of code
print(random.randint(5, 20))  # line 1
# random.randint - displays a random integer between the provided range (which is 5-20 in this case)
# the smallest number could have been 5 and the largest would have been 19
print(random.randrange(3, 10, 2))  # line 2
# random.randrange returns a random value from the given range, in this case the range is 3 to 10 with a step of 2
# the largest number we could've seen was 9 and the smallest would be 3
# No, line 2 cannot produce a 4 as the step has been set to 2 which means it can display numbers i+2
print(random.uniform(2.5, 5.5))  # line 3
# random.uniform produces a random float between the given range which is 2.5 to 5.5 in this case
# the smallest number could be observed is 2.5 and the largest would be 5.4

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 101))
