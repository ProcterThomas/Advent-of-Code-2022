import numpy as np

def print_grid(x, y):
    grid_max = max(x + y) + 1
    #grid = [['.']*grid_max]*grid_max
    grid = np.zeros((grid_max, grid_max)).tolist()

    for i in range(len(x)-1, -1, -1):
        grid[y[i]][x[i]] = i
        if i == 0:
            grid[y[i]][x[i]] = 'H'
    
    for line in grid:
        print(line)




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

    for i in range(0, num):
        for j in range(0, len(x)):
            if j == 0:
                if d == 'R':
                    x[0] = x[0] + 1
                if d == 'L':
                    x[0] = x[0] - 1
                if d == 'U':
                    y[0] = y[0] + 1
                if d == 'D':
                    y[0] = y[0] - 1

            if j != 0:
                dx = x[j-1]-x[j]
                dy = y[j-1]-y[j]

                for k in range(0, len(x_stat)):
                    if dx == x_stat[k] and dy == y_stat[k]:
                        x[j] = x[j] + x_move[k]
                        y[j] = y[j] + y_move[k]
                        break
                        
            if j == len(x)-1:
                t_coords.append((x[j], y[j]))
        
    print(x)
    print(y)
    print('-----------------')
    print_grid(x,y)

single_coords = []
for tc in t_coords:
    if tc not in single_coords:
        single_coords.append(tc)

print(len(single_coords))
