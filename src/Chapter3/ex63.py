# Exercise 63:Temperature Conversion Table
# (22 Lines)
# Write a program that displays a temperature conversion table for degrees Celsius and
# degrees Fahrenheit. The table should include rows for all temperatures between 0
# and 100 degrees Celsius that are multiples of 10 degrees Celsius. Include appropriate
# headings on your columns. The formula for converting between degrees Celsius and
# degrees Fahrenheit can be found on the internet.
temp=0
while temp<=100:
    fahrenheit = temp * 9/5 + 32
    print("{0}  {1:.2f}".format(temp, fahrenheit))
    temp += 10
