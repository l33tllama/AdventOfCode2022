def get_outcome(op, result):
    # A - rock B - paper C - scissors
    me = ""
    # I'm too lazy atm
    if result == "X": # Lose
        if op == "A": # Rock
            me = "Z"
        elif op == "B": # Paper
            me = "X"
        elif op == "C": #Scissors
            me = "Y"
    elif result == "Y": # Draw
        if op == "A":
            me = "X"
        elif op == "B":
            me = "Y"
        elif op == "C":
            me = "Z"
    elif result == "Z": # Win
        if op == "A": # Rock
            me = "Y"
        elif op == "B": # Paper
            me = "Z"
        elif op == "C":
            me = "X"
    return me
        
def check_line(op, result):
    shape_score = 0
    round_score = 0
    if result == "X":
        round_score = 0
    elif result == "Y":
        round_score = 3
    elif result == "Z":
        round_score = 6
    me = get_outcome(op, result)
    if me == "X": # Rock
        shape_score = 1
    elif me == "Y": # Paper
        shape_score = 2
    elif me == "Z": # Paper
        shape_score = 3
    return shape_score + round_score

with open("input-2.txt") as rps_results:
    lines = rps_results.readlines()
    games_scores = 0
    for i in range(0, len(lines)):
        game = []
        opponent = lines[i][0]
        desired_result = lines[i][2]
        result = check_line(opponent, desired_result)
        games_scores += result
    print(str(games_scores))