# CALCULATE AND OUPTUT EXACT CHANGE FOR PROVIDED INTEGER INPUT #

# Take integer input
total_change = int(input())

# Account for no change
if total_change <= 0:
    print('No change')

# Initialize variables
dollars = 0
quarters = 0
dimes = 0
nickles = 0
pennies = 0

# Calculate change denominations and output results on individual lines
dollars = total_change // 100
if dollars > 0 and total_change > 0:
    total_change = total_change - (dollars * 100)
if dollars == 1:
    print(dollars, 'Dollar')
elif dollars > 1:
    print(dollars, 'Dollars')

quarters = total_change // 25
if quarters > 0 and total_change > 0:
    total_change = total_change - (quarters * 25)
if quarters == 1:
    print(quarters, 'Quarter')
elif quarters > 1:
    print(quarters, 'Quarters')

dimes = total_change // 10
if dimes > 0 and total_change > 0:
    total_change = total_change - (dimes * 10)
if dimes == 1:
    print(dimes, 'Dime')
elif dimes > 1:
    print(dimes, 'Dimes')

nickels = total_change // 5
if nickels > 0 and total_change > 0:
    total_change = total_change - (nickels * 5)
if nickels == 1:
    print(nickels, 'Nickel')
elif nickels > 1:
    print(nickels, 'Nickels')
    
pennies = total_change // 1
if pennies > 0 and total_change > 0:
    total_change = total_change - (pennies * 1)
if pennies == 1:
    print(pennies, 'Penny')
elif pennies > 1:
    print(pennies, 'Pennies')
