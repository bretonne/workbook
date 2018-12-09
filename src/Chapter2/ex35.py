# Exercise 35: Dog Years
# (22 Lines)
# It is commonly said that one human year is equivalent to 7 dog years. However this
# simple conversion fails to recognize that dogs reach adulthood in approximately two
# years. As a result, some people believe that it is better to count each of the first two
# human years as 10.5 dog years, and then count each additional human year as 4 dog
# years.
# Write a program that implements the conversion from human years to dog years
# described in the previous paragraph. Ensure that your program works correctly for
# conversions of less than two human years and for conversions of two or more human
# years. Your program should display an appropriate error message if the user enters
# a negative number.
humanYear = int(input("year:"))
if humanYear<0:
    print("Year cannot be a negative number")
elif humanYear <=2:
    print("dogYear: {0}".format(10.5 * humanYear))
else:
    print("dogYear: {0}".format(10.5 * 2 + (humanYear-2)*4))


