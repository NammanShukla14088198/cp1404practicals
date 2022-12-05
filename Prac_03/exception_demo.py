"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the user does not enter a valid integer in either of the inputs
2. When will a ZeroDivisionError occur?
when the user will enter zero in the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, You can change the possibility of a ZeroDivisionError by :
if denominator !=0
z = numerator/denominator
else 0
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

