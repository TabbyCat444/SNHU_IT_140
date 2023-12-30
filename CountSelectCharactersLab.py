# COUNT INPUT LENGTH WITHOUT SPACES, COMMAS, OR PERIODS #

# Take user input
user_text = input()

# Declare variables
char_count = 0
comma = ','
space = ' '
period = '.'

# Iterate through input and increment counter for every character that is to be counted
for t in range(len(user_text)):
    if comma == user_text[t]:
        char_count += 0
    elif space == user_text[t]:
        char_count += 0
    elif period == user_text[t]:
        char_count += 0
    else:
        char_count += 1

# Output character count
print(char_count)
