file = 'input_2.txt'
f = open(file)
text = f.readlines()

hx = 0
hy = 0

tx = 0
ty = 0

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
        if d == 'R':
            hx = hx + 1
        if d == 'L':
            hx = hx - 1
        if d == 'U':
            hy = hy + 1
        if d == 'D':
            hy = hy - 1

        dx = hx-tx
        dy = hy-ty

        for k in range(0, len(x_stat)):
            if dx == x_stat[k] and dy == y_stat[k]:
                tx = tx + x_move[k]
                ty = ty + y_move[k]
                break

        t_coords.append((tx, ty))

single_coords = []
for tc in t_coords:
    if tc not in single_coords:
        single_coords.append(tc)

print(len(single_coords))
