# REFORMAT INPUT NAME #

# Get user name
user_name = input()
# Create list of user name split at the spaces
name_list = user_name.split()

# Assign first, middle, and last name variables
first_ini = name_list[0][0]
middle_ini = name_list[1][0]
last_name = name_list[-1]

# Output reformatted name
if len(name_list) == 3:
    print(last_name + ',', first_ini + '.' + middle_ini + '.')

else:
    print(last_name + ',', first_ini + '.')
