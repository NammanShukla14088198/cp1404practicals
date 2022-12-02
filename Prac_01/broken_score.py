"""
CP1404 - Practical
Broken program to determine score status
"""
# TODO: Fix this!

score = float(input("Enter score: "))
if 0 > score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
