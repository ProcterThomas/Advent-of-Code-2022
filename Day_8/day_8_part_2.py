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

scores = []
for x in range(0, x_trees):
    for y in range(0, y_trees):
        tree_h = block[y][x]

        # Check North
        N_scenic = 0
        for i in range(y-1, -1, -1):
            if block[i][x] >= tree_h:
                N_scenic = N_scenic + 1
                break
            else:
                N_scenic = N_scenic + 1

        # Check East
        E_scenic = 0
        for i in range(x+1, x_trees):
            if block[y][i] >= tree_h:
                E_scenic = E_scenic + 1
                break
            else:
                E_scenic = E_scenic + 1

        # Check South
        S_scenic = 0
        for i in range(y+1, y_trees):
            if block[i][x] >= tree_h:
                S_scenic = S_scenic + 1
                break
            else:
                S_scenic = S_scenic + 1

        # Check West
        W_scenic = 0
        for i in range(x-1, -1, -1):
            if block[y][i] >= tree_h:
                W_scenic = W_scenic + 1
                break
            else:
                W_scenic = W_scenic + 1

        scenic_score = N_scenic * E_scenic * S_scenic * W_scenic

        scores.append(scenic_score)

print(max(scores))