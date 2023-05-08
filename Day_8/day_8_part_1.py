file = 'input_2.txt'
f = open(file)
text = f.readlines()

block = []
for line in text:
    if '\n' in line:
        line = line.split('\n')[0]
    row = []
    for tree in line:
        row.append(tree)
    block.append(row)

x_trees = len(block[0])
y_trees = len(block)

vis_internal_trees = 0
for x in range(0, x_trees):
    for y in range(0, y_trees):
        tree_h = block[y][x]

        # Check North
        N_vis = 1
        for i in range(0, y):
            if block[i][x] >= tree_h:
                N_vis = 0

        # Check East
        E_vis = 1
        for i in range(x+1, x_trees):
            if block[y][i] >= tree_h:
                E_vis = 0

        # Check South
        S_vis = 1
        for i in range(y+1, y_trees):
            if block[i][x] >= tree_h:
                S_vis = 0

        # Check West
        W_vis = 1
        for i in range(0, x):
            if block[y][i] >= tree_h:
                W_vis = 0

        vis = N_vis + E_vis + S_vis + W_vis

        if vis > 0:
            vis_internal_trees = vis_internal_trees + 1

print(vis_internal_trees)
