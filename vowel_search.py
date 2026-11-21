"""Finds vowels occurring in a word."""

vowel = ['a','e','i','o','u']
word = input("Provide a word to search for vowel: ")

found = []

for letter in word:
    if letter in vowel:
        if letter not in found:
            found.append(letter)
print(found)
