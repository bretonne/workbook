# Exercise 4:Area of a Field
# (Solved—15 Lines)
# Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.
# Hint: There are 43,560 square feet in an acre.
len_input = input("Length in foot:")
length = int(len_input)
wid_input = input("width in foot:")
width = int(wid_input)
area = length*width/43560
print("The area of the field is {0:.2f} acres".format(area))
