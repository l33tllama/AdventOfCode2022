with open("input-1.txt") as inputs:
    lines = inputs.readlines()
    current_elf_calories = 0
    elf_calories = []
    for i in range(0, len(lines)):
        line = lines[i]
        if line != "\n":
            value = int(line)
            current_elf_calories += value
        else:
            elf_calories.append(current_elf_calories)
            current_elf_calories = 0
    elf_calories = sorted(elf_calories)
    top_three = elf_calories[len(elf_calories)-1]
    top_three += elf_calories[len(elf_calories)-2]
    top_three += elf_calories[len(elf_calories)-3]
    print(str(top_three))