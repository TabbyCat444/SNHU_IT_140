# CREATE A PASSWORD WITH CERTAIN REQUIRMENTS FROM USER INPUT #

# Takes user input for a flower, color, and number
favorite_color = str(input("Please enter a color: "))
favorite_flower = str(input("Please enter a flower: "))
favorite_number = str(input("Please enter a number: "))

# Output all the values on a single line
print('You entered: ' + favorite_color + ' ' + favorite_flower + ' ' + favorite_number)


# Output two password options
password1 = favorite_color + '_' + favorite_flower
password2 = favorite_number + favorite_color + favorite_number
print('\nFirst password: ' + password1)
print('Second password: ' + password2)


# Output the length of the two password options
print('\nNumber of characters in', password1 + ':', len(password1))
print('Number of characters in', password2 + ':', len(password2))
