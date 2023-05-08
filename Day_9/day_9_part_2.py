file = 'input_1.txt'
f = open(file)
text = f.readlines()

x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

x_stat = [-1, 0, 1, 2, 2, 2, 1, 0, -1, -2, -2, -2]
y_stat = [2, 2, 2, 1, 0, -1, -2, -2, -2, -1, 0, 1]

x_move = [-1, 0, 1, 1, 1, 1, 1, 0, -1, -1, -1, -1]
y_move = [1, 1, 1, 1, 0, -1, -1, -1, -1, -1, 0, 1]

t_coords = []

for line in text:
    if '\n' in line:
        line = line.split('\n')[0]
    
    d, num = line.split(' ')

    num = int(num)

    for j in range(0, len(x)):
        for i in range(0, num):
            if j == 0:
                if d == 'R':
                    x[j] = x[j] + 1
                if d == 'L':
                    x[j] = x[j] - 1
                if d == 'U':
                    y[j] = y[j] + 1
                if d == 'D':
                    y[j] = y[j] - 1

            if j != 0:
                dx = x[j-1]-x[j]
                dy = y[j-1]-y[j]

                for k in range(0, len(x_stat)):
                    if dx == x_stat[k] and dy == y_stat[k]:
                        x[j] = x[j] + x_move[k]
                        y[j] = y[j] + y_move[k]
                        break
                if j == len(x):
                    t_coords.append((x[j], y[j]))
    print(x)
    print(y)
    print('\n')

single_coords = []
for tc in t_coords:
    if tc not in single_coords:
        single_coords.append(tc)

# print(x)
# print(y)
