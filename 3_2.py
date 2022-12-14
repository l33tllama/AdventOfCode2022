def find_in_three(a, b, c):
    loc = -1
    for ch in a:
        if ch in b:
            if ch in c:
                loc = c.find(ch)
    if loc > -1:
        return c[loc]
    else:
        return None

with open("input-3.txt") as rs_items:
    lines = rs_items.readlines()
    total_priority = 0
    line_1, line_2, line_3 = "", "", ""
    i = 0
    while i < len(lines):
        line_1 = lines[i][:len(lines[i])-1]
        line_2 = lines[i+1][:len(lines[i+1])-1]
        line_3 = lines[i+2][:len(lines[i+2])-1]
        c = find_in_three(line_1, line_2, line_3)
        if c:
            char_num = ord(c)
            priority = 0
            # lower case
            if char_num > 96 and char_num < 123:
                priority = char_num - 96
            elif char_num > 64 and char_num < 91:
                priority = 27 + char_num - 65
            total_priority += priority
        # Increment
        i += 3
    print(total_priority)
