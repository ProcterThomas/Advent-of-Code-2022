file = 'input_2.txt'
f = open(file)
text = f.readlines()

contain_count = 0
for i in range(0, len(text)):
    elf_1_s = int(text[i].split(',')[0].split('-')[0])
    elf_1_e = int(text[i].split(',')[0].split('-')[1])
    elf_2_s = int(text[i].split(',')[1].split('-')[0])
    elf_2_e = int(text[i].split(',')[1].split('-')[1])

    if elf_1_s <= elf_2_s and elf_1_e >= elf_2_e:
        contain = 1
    elif elf_2_s <= elf_1_s and elf_2_e >= elf_1_e:
        contain = 1
    else:
        contain = 0

    contain_count = contain_count + contain

print(contain_count)