# DRAWS A RIGHT TRIANGLE WITH USER CHOICE OF CHARACTER #

# Get triangle character and height
triangle_char = input('Enter a character:\n') + ' '
triangle_height = int(input('Enter triangle height:\n\n'))

# Set triangle line
triangle_line = triangle_char

# Use character and height to print triangle
while triangle_height > 0:
    print(triangle_line)
    triangle_height -= 1
    triangle_line = triangle_line + triangle_char
