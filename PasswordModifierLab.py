# MODIFY USER PROVIDED PASSWORD FOR BETTER SECURITY #

word = input()
password = word

'''
.replace('i', '!')
.replace('a', '@')
.replace('m', 'M')
.replace('B', '8')
.replace('o', '.')
+ 'q*s' to the end
'''
for i in range(len(word)):
    if password[i] == 'i':
        password = password.replace('i', '!')
    if password[i] == 'a':
        password = password.replace('a', '@')
    if password[i] == 'm':
        password = password.replace('m', 'M')
    if password[i] == 'B':
        password = password.replace('B', '8')
    if password[i] == 'o':
        password = password.replace('o', '.')

# print password
print('{}q*s'.format(password))
