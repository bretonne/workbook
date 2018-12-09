# Exercise 136:Anagrams Again
# (48 Lines)
# The notion of anagrams can be extended to multiple words. For example, “William
# Shakespeare” and “I am a weakish speller” are anagrams when capitalization and
# spacing are ignored.
# 66 6 Dictionary Exercises
# Extend your program from Exercise 135 so that it is able to check if two phrases
# are anagrams. Your program should ignore capitalization, punctuation marks and
# spacing when making the determination.

def isAnagrams(word1, word2):
    letterMap = {}
    for letter in word1:
        if letter in letterMap:
            letterMap[letter] += 1
        else:
            letterMap[letter] = 1

    for letter in word2:
        if letter in letterMap:
            letterMap[letter] -= 1
        else:
            return False

    for count in letterMap.values():
        if count > 0:
            return False
    return True



def trim(word:str):
    trimmed = []
    for letter in word:
        if (letter.isalpha()):
            trimmed.append(letter.lower())
    wholeword = "".join(trimmed)
    print(wholeword)
    return wholeword


def main():
    word1 = input("sentence 1:")
    word2 = input("sentence 2:")

    trimmed1=trim(word1)
    trimmed2 = trim(word2)

    print("Is Anagrams:", isAnagrams(trimmed1, trimmed2))

main()