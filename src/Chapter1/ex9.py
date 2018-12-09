# Exercise 9: Compound Interest
# (19 Lines)
# Pretend that you have just opened a new savings account that earns 4 percent interest
# per year. The interest that you earn is paid at the end of the year, and is added
# to the balance of the savings account. Write a program that begins by reading the
# amount of money deposited into the account from the user. Then your program should
# compute and display the amount in the savings account after 1, 2, and 3 years. Display
# each amount so that it is rounded to 2 decimal places.
depositStr = input("deposit:")
balance = float(depositStr)
print("Initial deposit: {0:.2f}".format(balance))
balance *= (1+4/100)
print("Balance after 1 year: {0:.2f}".format(balance))
balance *= (1+4/100)
print("Balance after 2 years: {0:.2f}".format(balance))
balance *= (1+4/100)
print("Balance after 3 year: {0:.2f}".format(balance))