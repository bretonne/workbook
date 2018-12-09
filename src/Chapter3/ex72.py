# Exercise 72: Is a String a Palindrome?
# (Solved—23 Lines)
# A string is a palindrome if it is identical forward and backward. For example “anna”,
# “civic”, “level” and “hannah” are all examples of palindromicwords. Write a program
# that reads a string from the user and uses a loop to determines whether or not it is a
# palindrome. Display the result, including a meaningful output message.

# word = input("Please enter a word:\n")
# reverseWord=""
# length = len(word)
# for i in range(0, length):
#     reverseWord += word[length-1-i]
#
# print("isPalindrom: ", (reverseWord==word))

word = input("Please enter a word:\n")
length = len(word)
isPalindrom = True

for i in range(0, length):
    if (word[i] != word[length-1-i]):
        isPalindrom = False
        break
print("isPalindrom: ", isPalindrom)
