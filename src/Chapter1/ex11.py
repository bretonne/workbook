# Exercise 11: Fuel Efficiency
# (13 Lines)
# In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon
# (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
# kilometers (L/100 km). Use your research skills to determine how to convert from
# MPGto L/100 km. Then create a program that reads a value from the user in American
# units and displays the equivalent fuel efficiency in Canadian units.
Liter_Per_Gallon = 3.7854
Km_Per_Mile = 1.61

mpg=float(input("mpg:"))
literPer100Km = 100/Km_Per_Mile / mpg * Liter_Per_Gallon
print("Canadian Fuel efficiency Liter Per 100 Km = {0:.2f}".format(literPer100Km))
