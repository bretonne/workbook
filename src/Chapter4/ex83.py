# Exercise 83: Shipping Calculator
# (23 Lines)
# An online retailer provides express shipping for many of its items at a rate of $10.95
# for the first item, and $2.95 for each subsequent item. Write a function that takes the
# number of items in the order as its only parameter. Return the shipping charge for
# the order as the function’s result. Include a main program that reads the number of
# items purchased from the user and displays the shipping charge.
def shippingcost(itemCount):
    if (itemCount==0):
        return 0
    else:
        return 10.95 + (itemCount-1)*2.95

count = int(input("Please enter item count:\n"))
print("Shipping cost is : {0:.2f}".format(shippingcost(count)))