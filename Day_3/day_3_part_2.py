file = 'input_2.txt'
f = open(file)
text = f.readlines()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
           'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

priorities = 0

for i in range(0, len(text)):
    if i%3 == 0:
        sack_1 = text[i].split('\n')[0]
        sack_2 = text[i+1].split('\n')[0]
        sack_3 = text[i+2].split('\n')[0]

        for item in sack_1:
            if item in sack_2 and item in sack_3:
                d_item = item
                break

        priority = letters.index(d_item) + 1
        priorities = priorities + priority

print(priorities)