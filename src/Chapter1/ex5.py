# Exercise 5: Bottle Deposits
# (Solved—15 Lines)
# In many jurisdictions a small deposit is added to drink containers to encourage people
# to recycle them. In one particular jurisdiction, drink containers holding one liter or
# less have a $0.10 deposit, and drink containers holding more than one liter have a
# $0.25 deposit.
# Write a program that reads the number of containers of each size from the user.
# Your program should continue by computing and displaying the refund that will be
# received for returning those containers. Format the output so that it includes a dollar
# sign and always displays exactly two decimal places.
input_count_small = input("Number of containers that are one liter or less:")
count_oneliter_less = int(input_count_small)
input_count_big = input("Number of containers that are more than one liter:")
count_oneliter_more = int(input_count_big)
refund = 0.1 * count_oneliter_less + 0.25 * count_oneliter_more
print("Your refund amount is ${0:.2f}".format(refund))