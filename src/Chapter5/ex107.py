# Exercise 107:Avoiding Duplicates
# (Solved—21 Lines)
# In this exercise, you will create a program that reads words from the user until the
# user enters a blank line. After the user enters a blank line your program should display
# each word entered by the user exactly once. The words should be displayed in
# the same order that they were entered. For example, if the user enters:
# first
# second
# first
# third
# second
# then your program should display:
# first
# second
# third
def getInputs():
    words=[]
    line = input()
    while line != "" :
        words.append(line)
        line = input()
    return words

def wordExists(words, myword):
    for word in words:
        if (word== myword):
            return True
    return False


words = getInputs()
unique = []
for word in words:
    if (wordExists(unique, word)==False):
        unique.append(word)
print(unique)