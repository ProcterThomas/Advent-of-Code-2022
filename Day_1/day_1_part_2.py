file = 'input_2.txt'
f = open(file)
text = f.readlines()

total_cal = []
cals = 0
for line in text:
    if line != '\n':
        cals = cals + int(line)
    else:
        total_cal.append(cals)
        cals = 0

total_cal.append(cals)

total_cal.sort()

top_3 = sum(total_cal[-3:])

print(top_3)
