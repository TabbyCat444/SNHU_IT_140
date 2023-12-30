# OUTPUT MAX AND AVERAGE VALUES FROM USER LIST OF INTEGERS #

user_input = input()
my_list = [int(i) for i in user_input.split()]

max_num = max(my_list)
avg_num = int((sum(my_list) / len(my_list)))

print(avg_num, max_num)
