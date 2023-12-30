# FILTER NEGATIVE NUMBERS FROM USER INPUT LIST AND SORT THEM IN ASCENDING ORDER #

user_input = input()
my_list = [int(i) for i in user_input.split()]

no_neg = []

for i in my_list:
    if i >= 0:
        no_neg == no_neg.append(i)

final_nums = sorted(no_neg)

print(*final_nums, end = ' ')
