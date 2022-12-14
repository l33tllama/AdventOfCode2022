def solve_rps(me, op):
    # Win conditions
    success = (me == "R" and op == "S")
    success = success or (me == "P" and op == "R")
    success = success or (me == "S" and op == "P")
    if success:
        return "success"
    else:
        tie = (me == "R" and op == "R")
        tie = tie or (me == "P" and op == "P")
        tie = tie or (me == "S" and op == "S")
        if tie:
            return "tie"
    return "defeat"

def check_line(op, me):
    shape_score = 0
    round_score = 0
    op_rps = ""
    me_rps = ""
    if me == "X": # Rock
        shape_score = 1
        me_rps = "R"
    elif me == "Y": # Paper
        shape_score = 2
        me_rps = "P"
    elif me == "Z": # Paper
        shape_score = 3
        me_rps = "S"
    if op == "A":
        op_rps = "R"
    elif op == "B":
        op_rps = "P"
    elif op == "C":
        op_rps = "S"
    result = solve_rps(me_rps, op_rps)
    if result == "success":
        round_score = 6
    elif result == "tie":
        round_score = 3
    elif result == "defeat":
        round_score = 0
    return shape_score + round_score

with open("input-2.txt") as rps_results:
    lines = rps_results.readlines()
    games_scores = 0
    for i in range(0, len(lines)):
        game = []
        opponent = lines[i][0]
        yours = lines[i][2]
        result = check_line(opponent, yours)
        #print(result)
        games_scores += result
    print(str(games_scores))            