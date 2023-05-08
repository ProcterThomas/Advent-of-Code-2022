import numpy as np

class command:
    def __init__(self, string):
        self.many = int(string.split(' ')[1])
        self.orig = int(string.split(' ')[3])
        self.dest = int(string.split(' ')[5].split('\n')[0])

def move_crates(dock, command, plat):
    many = command.many
    orig = command.orig
    dest = command.dest

    dest_arrival = 'nan'
    for i in range(0, plat**2):
        if dock[i][dest-1] != 0.0:
            dest_arrival = i - 1
            break
    
    if dest_arrival == 'nan':
        dest_arrival = plat**2 - 1

    for j in range(0, many):
        for i in range(0, plat**2):
            if dock[i][orig-1] != 0.0:
                crate = dock[i][orig-1]
                dock[i][orig-1] = 0.0
                break

        dock[dest_arrival-(many-(j+1))][dest-1] = crate

    return dock

def read_dock(dock, plat):
    message = []
    for j in range(0, plat):
        letter = 'nan'
        for i in range(0, plat**2):
            if dock[i][j] != 0.0:
                letter = dock[i][j]
                break
        if letter == 'nan':
            letter = ' '
        
        message.append(letter)

    message = ''.join(message)

    return message


file = 'input_2.txt'
f = open(file)
text = f.readlines()

commands = []
for line in text:
    if 'move' in line:
        commands.append(command(line))

plat = int(len(text[0])/4)

dock = np.zeros((plat**2, plat))

for i in range(0, len(text)):
    if text[i] == '\n':
        line_break = i
        break

crate_line = line_break - 2

dock = dock.tolist()

for j in range(0, crate_line + 1):
    for i in range(0, plat):
        crate = text[crate_line - j][i*4 + 1]
        if crate == ' ':
            crate = 0.0
        dock[-(1 + j)][i] = crate

for thing in commands:
    dock = move_crates(dock, thing, plat)

for line in dock:
    print(line)

message = read_dock(dock, plat)
print(message)