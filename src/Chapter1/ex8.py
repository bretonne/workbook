# Exercise 8:Widgets and Gizmos
# (15 Lines)
# An online retailer sells two products: widgets and gizmos. Each widget weighs 75
# grams. Each gizmo weighs 112 grams. Write a program that reads the number of
# widgets and the number of gizmos in an order from the user. Then your program
# should compute and display the total weight of the order.
wStr = input("numbwer of widgets:")
gStr = input("number of gizmos:")
nOfwidgets = int(wStr)
nOfgizmos = int(gStr)
totalWeight = 75 * nOfwidgets + 112 * nOfgizmos
print("Total weight: {0:.0f}".format(totalWeight))