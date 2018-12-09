# Exercise 104: Sorted Order
# (Solved—21 Lines)
# Write a program that reads integers from the user and stores them in a list. Your
# program should continue reading values until the user enters 0. Then it should display
# all of the values entered by the user (except for the 0) in order from smallest to largest,
# with one value appearing on each line. Use either the sort method or the sorted
# function to sort the list.
numbers=[]
a=int(input("Number: "))
while a!=0:
    numbers.append(a)
    a = int(input("Number: "))
numbers.sort()
print(numbers)