"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))
if sales <= 1000:
    bonus_10 = sales/100 * 10
    print("Your Bonus is:", bonus_10)
else:
    bonus_15 = sales/100 * 15
    print("Your Bonus is:", bonus_15)