# SWAP TWO USER PROVIDED INTEGERS #

def swap_values(user_val1, user_val2):
    switch = user_val1
    user_val1 = user_val2
    user_val2 = switch
    return user_val1, user_val2

if __name__ == '__main__': 
    num1 = int(input())
    num2 = int(input())
    
    num1, num2 = swap_values(num1, num2)
    
    print(num1, num2)
