# Exercise 135:Anagrams
# (Solved—39 Lines)
# Two words are anagrams if they contain all of the same letters, but in a different
# order. For example, “evil” and “live” are anagrams because each contains one e, one
# i, one l, and one v. Create a program that reads two strings from the user, determines
# whether or not they are anagrams, and reports the result.

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



def isAnagramsBySort(word1, word2):
    letters1 = word1.split()
    letters2 = word2.split()
    letters1.sort()
    letters2.sort()
    print(letters1)
    print(letters2)
    sorted1 = "".join(letters1)
    sorted2 = "".join(letters2)
    print("{0}  {1}".format(sorted1, sorted2))

    return sorted1 == sorted2


def main():
    word1 = input("word1:")
    word2 = input("word2:")

    print("Is Anagrams:", isAnagrams(word1, word2))

main()