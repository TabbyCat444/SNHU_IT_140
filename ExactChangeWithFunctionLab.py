# CALCULATE AND DISPLAY EXACT CHANGE FOR PROVIDED INPUT USING A FUNCTION #

def exact_change(user_total):
    if user_total <= 0:
    	return print('no change')
    elif user_total > 0:
    	num_dollars = user_total // 100
    	user_total = user_total % 100
    	if num_dollars == 1:
    		print(num_dollars, 'dollar')
    	if num_dollars > 1:
    		print(num_dollars, 'dollars')
    	num_quarters = user_total // 25
    	user_total = user_total % 25
    	if num_quarters == 1:
    		print(num_quarters, 'quarter')
    	if num_quarters > 1:
    		print(num_quarters, 'quarters')
    	num_dimes = user_total // 10
    	user_total = user_total % 10
    	if num_dimes == 1:
    		print(num_dimes, 'dime')
    	if num_dimes > 1:
    		print(num_dimes, 'dimes')
    	num_nickels = user_total // 5
    	user_total = user_total % 5
    	if num_nickels == 1:
    		print(num_nickels, 'nickel')
    	if num_nickels > 1:
    		print(num_nickels, 'nickels')
    	num_pennies = user_total // 1
    	user_total = user_total % 1
    	if num_pennies == 1:
    		print(num_pennies, 'penny')
    	if num_pennies > 1:
    		print(num_pennies, 'pennies')
    	return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies

if __name__ == '__main__': 
    input_val = int(input())    
    for amount in exact_change(input_val):
    	if amount == 0:
    		continue
