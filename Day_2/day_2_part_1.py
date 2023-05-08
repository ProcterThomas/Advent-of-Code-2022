file = 'input_2.txt'
f = open(file)
text = f.readlines()

points = 0
for i in range(0, len(text)):
    game = text[i].split('\n')[0]

    if game == 'A X':
        point = 1 + 3
    elif game == 'A Y':
        point = 2 + 6
    elif game == 'A Z':
        point = 3 + 0
    elif game == 'B X':
        point = 1 + 0
    elif game == 'B Y':
        point = 2 + 3
    elif game == 'B Z':
        point = 3 + 6
    elif game == 'C X':
        point = 1 + 6
    elif game == 'C Y':
        point = 2 + 0
    elif game == 'C Z':
        point = 3 + 3
    else:
        print('game not cataloged!')

    points = points + point

print(points)