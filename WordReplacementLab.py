# REPLACE WORDS IN A SENTENCE WITH DESIGNATED OPTION #

replace_pairs = input().split()
sentence = input()

org_word = replace_pairs[0::2]
rep_word = replace_pairs[1::2]

for org, rep in zip(org_word, rep_word):
    sentence = sentence.replace(org, rep)

print(sentence)
