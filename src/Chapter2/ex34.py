# Exercise 34: Even or Odd?
# (Solved—13 Lines)
# Write a program that reads an integer from the user. Then your program should
# display a message indicating whether the integer is even or odd.
num = int(input("number:"))
if num % 2 == 0 :
    print(num, " is an event number")
else:
    print(num, " is an odd number")
