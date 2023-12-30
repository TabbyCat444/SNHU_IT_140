# PRACTICE TAKING AND COMBINING VARIOUS INPUTS THEN OUTPUTTING THE RESULT #

# Takes user inputs for an integer between 32 and 126, a float, a character, and a string
user_int = int(input('Enter integer (32 - 126):\n'))
user_float = input('Enter float:\n')
user_char = input('Enter character:\n')
user_str = input('Enter string:\n')

# Ouputs user input on one line
print(user_int, user_float, user_char, user_str)

print(user_str, user_char, user_float, user_int)

print(user_int, 'converted to a character is', chr(user_int))
