file = 'input_2.txt'
f = open(file)
text = f.readlines()

points = 0
for i in range(0, len(text)):
    game = text[i].split('\n')[0]

    if game == 'A X':
        point = 0 + 3
    elif game == 'A Y':
        point = 3 + 1
    elif game == 'A Z':
        point = 6 + 2
    elif game == 'B X':
        point = 0 + 1
    elif game == 'B Y':
        point = 3 + 2
    elif game == 'B Z':
        point = 6 + 3
    elif game == 'C X':
        point = 0 + 2
    elif game == 'C Y':
        point = 3 + 3
    elif game == 'C Z':
        point = 6 + 1
    else:
        print('game not cataloged!')

    points = points + point

print(points)