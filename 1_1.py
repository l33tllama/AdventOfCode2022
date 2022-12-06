lines = open("input-1.txt").readlines()
current_elf_calories, elf_calories = 0, []
for i in range(0, len(lines)):
    if lines[i] != "\n":
        current_elf_calories += int(lines[i])
    else:
        elf_calories.append(current_elf_calories)
        current_elf_calories = 0
elf_calories = sorted(elf_calories)
print(str(elf_calories[len(elf_calories)-1]))