
def find_char_in_both(a, b):
    loc = -1
    for c in a:
        if c in b:
            loc = b.find(c)
    if loc > -1:
        return b[loc]
    else:
        return None

with open("input-3.txt") as rs_items:
    lines = rs_items.readlines()
    total_priority = 0
    for i in range(0, len(lines)):
        line = lines[i][:len(lines[i])-1]
        
        line_1 = line[:int(len(line)/2)]
        line_2 = line[int(len(line)/2):]
        
        c = find_char_in_both(line_1, line_2)
        if c:
            char_num = ord(c)
            priority = 0
            # lower case
            if char_num > 96 and char_num < 123:
                priority = char_num - 96
            elif char_num > 64 and char_num < 91:
                priority = 27 + char_num - 65
            total_priority += priority
    print(total_priority)