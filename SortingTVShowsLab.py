# READ IN LIST OF TV SHOWS AND HOW MANY SEASONS THEY HAVE, THEN SORT LIST BY NUMBER OF SEASONS IN ASCENDING ORDER USING A DICTIONARY #

input = input()

with open(input) as labinput:
    shows = labinput.readlines()

dict = {}
        
for i in range(0, len(shows )-1, 2):
    nums = int(shows[i].strip())
    title = shows[i+1].strip()
    if(nums in dict):
        dict[nums].append(title)
    else:
        dict[nums] = [title]
        
keys = list(dict.keys())
keys.sort()
with open('output_keys.txt', 'w') as outputkeys:
    for key in keys:
        names = '; '.join(title for title in dict[key])
        outputkeys.write(str(key)+': '+names + "\n")
names = []
for item in dict:
    for name in dict[item]:
        names.append(name)

names.sort()
with open('output_titles.txt', 'w') as outputtitles:
    for name in names:
        outputtitles.write(name + '\n')
