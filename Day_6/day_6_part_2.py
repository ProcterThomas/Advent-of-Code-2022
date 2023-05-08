file = 'input_2.txt'
f = open(file)
text = f.readline()

for k in range(14, len(text)):
    pack = text[k-14:k]

    badness = 0
    for i in range(0, len(pack)):
        for j in range(0, len(pack)):
            if i != j:
                if pack[i] == pack[j]:
                    badness = 1

    if badness == 0:
        start_pos = k
        break

print(start_pos)