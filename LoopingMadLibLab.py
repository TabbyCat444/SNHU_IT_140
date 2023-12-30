# TAKES USER INPUT OF A STRING AND AN INTEGER UNTIL USER QUITS THEN PRINTS FUNNY SENTENCE USING EACH INPUT #

# accept user input of str + int
user_strint = input()
user_strint = user_strint.split()

# print 'Eating {} {} a day keeps the doctor away.'.format(int, str), repeat until user inputs 'quit' as the str
while user_strint[0] != 'quit':
    print('Eating {} {} a day keeps the doctor away.'.format(user_strint[1], user_strint[0]))
    user_strint = input()
    user_strint = user_strint.split()
