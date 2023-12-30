# LAB FOR COUNTING THE NUMBER OF INSTANCES OF A DESIGNATED CHARACTER FROM INPUT #

# Takes user input to as a character to count and a phrase to search through in one line
user_text = input("Please enter a single character to count followed by a space and then a word or phrase to count the"
                  " character in: ")

# Outputs the number of times that character is in the designated phrase
print("Your character is present this many times: ", + user_text[1:].count(user_text[0:1]))
