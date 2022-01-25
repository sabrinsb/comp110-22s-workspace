"""EX01 - Chardle - A  cute step toward Wordle."""
__author__ = "730221505"

from cmath import sin


word_choice: str = input("Enter a 5-character word: ")
if len(word_choice) != 5: 
    print ("Invalid word " + word_choice + "Word must contain 5 characters")
    exit()
single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print ("Character must be a single character: ")
    exit()
print("Searching for " + single_character  + " in " + word_choice)

count = 0 
if word_choice[0] == single_character: 
    count = count + 1
    print(single_character + " found at index 0")
if word_choice[1] == single_character: 
    count = count + 1
    print(single_character + " found at index 1")
if word_choice[2] == single_character: 
    count = count + 1
    print(single_character + " found at index 2")
if word_choice[3] == single_character:
    count = count + 1
    print(single_character + " found at index 3")
if word_choice[4] == single_character:
    count = count + 1 
    print(single_character + " found at index 4")

if count > 0:
    print(str(count) + "instance of " + single_character + " found in " + word_choice)
else:
    print("No instance of " + single_character + " found in " + word_choice)