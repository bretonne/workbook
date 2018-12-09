# Exercise 61:Average
# (26 Lines)
# In this exercise you will create a program that computes the average of a collection
# of values entered by the user. The user will enter 0 as a sentinel value to indicate
# that no further values will be provided. Your program should display an appropriate
# error message if the first value entered by the user is 0.
# Hint: Because the 0 marks the end of the input it should not be included in the
# average.
count=0
sum=0
num=int(input("Number:"))
while num!=0:
    sum+=num
    count += 1
    num = int(input("Number:"))

average = sum/count
print("Average is " + average)
