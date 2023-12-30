# COUNT WORD FREQUENCY FROM LIST OF WORDS READ IN FROM A CSV FILE #

import csv

input = input()

with open(input, 'r') as labinput:
    input_reader = csv.reader(labinput)
    
    word_list = dict()
    
    for col in input_reader:
        for word in col:
            try:
                word_list[word] += 1
            except KeyError:
                word_list[word] = 1
    for word, count in word_list.items():
        print(word, count)
    
