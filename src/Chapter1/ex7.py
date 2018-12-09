# Exercise 7:Sum of the First n Positive Integers
# (Solved—12 Lines)
# Write a program that reads a positive integer, n, from the user and then displays the
# sum of all of the integers from 1 to n. The sum of the first n positive integers can be
# computed using the formula:
# sum = (n)(n + 1)
# 2
nStr = input("n:")
n = int(nStr)
sumOfNumbers = n*(n+1)/2
print("sum:{0:.0f}".format(sumOfNumbers))