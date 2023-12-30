# USER GUESSES NUMBER UNTIL CORRECT, COMPUTER INDICATES WHETHER VALUE SHOULD BE HIGHER OR LOWER #

import random

seedVal = int(input("What seed should be used? "))
random.seed(seedVal)

while True:
    low_input = int(input('What is the lower bound?'))
    high_input = int(input('What is the upper bound?'))

    lower = low_input
    upper = 0

    if high_input > lower:
        upper = high_input
        break
    else:
        print('Lower bound must be less than upper bound.')

winnernum = random.randint(lower, upper)

while True:
    guess = int(input('What is your guess?'))

    if guess < lower:
        print('Sorry, number must be between lower and upper bounds. Please try again.')

    elif guess > upper:
        print('Sorry, number must be between lower and upper bounds. Please try again.')

    elif guess < winnernum:
        print('Nope, too low.')

    elif guess > winnernum:
        print('Nope, too high.')

    elif guess == winnernum:
        print('You got it!')
        break
