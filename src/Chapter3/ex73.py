# Exercise 73: MultipleWord Palindromes
# (35 Lines)
# There are numerous phrases that are palindromes when spacing is ignored. Examples
# include “go dog”, “flee to me remote elf” and “some men interpret nine memos”,
# among many others. Extend your solution to Exercise 72 so that it ignores spacing
# while determining whether or not a string is a palindrome. For an additional challenge,
# extend your solution so that is also ignores punctuation marks and treats uppercase
# and lowercase letters as equivalent.

# word = input("Please enter a sentence:\n")
# reverseWord=""
# trimmedWord=""
# length = len(word)
# for i in range(0, length):
#     letter = word[length-1-i]
#     if (letter != " "):
#        reverseWord += letter
#     letter = word[i]
#     if (letter != " "):
#        trimmedWord += letter
# print("{0}, {1} isPalindrom: {2}".format(trimmedWord, reverseWord,  (trimmedWord==reverseWord)))


word = input("Please enter a sentence:\n")
length = len(word)
isPalindrom = True
trimmedWord=""

for i in range(0, length):
    letter = word[i]
    if (letter != " "):
        trimmedWord += letter

length = len(trimmedWord)
for i in range(0, length):
    if (trimmedWord[i] != trimmedWord[length-1-i]):
         isPalindrom = False
         break
print("isPalindrom: ", isPalindrom)
