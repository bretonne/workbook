# Exercise 106:Remove Outliers
# (Solved—43 Lines)
# When analysing data collected as part of a science experiment it may be desirable
# to remove the most extreme values before performing other calculations. Write a
# function that takes a list of values and an non-negative integer, n, as its parameters.
# The function should create a new copy of the list with the n largest elements and the
# n smallest elements removed. Then it should return the new copy of the list as the
# function’s only result. The order of the elements in the returned list does not have to
# match the order of the elements in the original list.
# Write a main program that demonstrates your function. Your function should read
# a list of numbers from the user and remove the two largest and two smallest values
# from it. Display the list with the outliers removed, followed by the original list. Your
# program should generate an appropriate error message if the user enters less than 4
# values.
def getInputs():
    numbers=[]
    a=int(input("Number: "))
    while a!=0:
        numbers.append(a)
        a = int(input("Number: "))
    return numbers

numbers = getInputs()
numbers.sort()
normalized = []
count = len(numbers)-2
for num in range(1, len(numbers)-1):
    normalized.append(numbers[num])
print(normalized)
print("count {0}, average {1:.2f}".format(count, sum(normalized)/count))
