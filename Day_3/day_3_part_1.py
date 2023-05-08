file = 'input_2.txt'
f = open(file)
text = f.readlines()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
           'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

priorities = 0

for i in range(0, len(text)):
    whole_line = text[i].split('\n')[0]
    line_length_half = int(len(whole_line)/2)

    sack_1 = whole_line[:line_length_half]
    sack_2 = whole_line[line_length_half:]

    for item in sack_1:
        if item in sack_2:
            d_item = item
            break

    priority = letters.index(d_item) + 1
    priorities = priorities + priority

print(priorities)