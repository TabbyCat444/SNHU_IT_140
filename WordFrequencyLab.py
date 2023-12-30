# OUTPUT THE FREQUENCY OF EACH WORD IN A USER INPUT LIST #

user_input = input()
list = user_input.split()

for i in list:
    num = list.count(i)
    print(i, num)
