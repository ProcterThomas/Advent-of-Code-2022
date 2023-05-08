file = 'input_2.txt'
f = open(file)
text = f.readlines()

def add_dir_size(thing, dir, size):
    try:
        thing[dir] = thing[dir] + size
    except KeyError:
        thing[dir] = size

dirs = {}
path = []
big_path = []

for i in range(0, len(text)):
    line = text[i].split('\n')[0]
    if ('$ cd' in line) and ('..' not in line):
        dir = line.split(' ')[2]
        path.append(dir)
        big_path.append('/'.join(path)[1:])
    elif '$ cd ..' in line:
        del path[-1]
        del big_path[-1]
    elif '$ ls' in line:
        pass
    elif 'dir' in line:
        pass
    else:
        size = int(line.split(' ')[0])
        for item in big_path:
            add_dir_size(dirs, item, size)

sizes = []
for item in dirs.keys():
    sizes.append(dirs[item])

total_size = 0
for size in sizes:
    if size < 100000:
        total_size = total_size + size

print(total_size)