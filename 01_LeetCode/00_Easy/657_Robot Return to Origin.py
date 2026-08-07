def judge_circle(moves: str) -> bool:
    # if len(moves) % 2 != 0:
    #     return False
    #
    # directions = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
    # track = [0, 0]
    # for move in moves:
    #     track[0] += directions[move][0]
    #     track[1] += directions[move][1]
    #
    # if track == [0, 0]:
    #     return True
    # else:
    #     return False

    return moves.count('U') == moves.count('D') and moves.count('R') == moves.count('L')



moves1 = "LL"
print(judge_circle(moves1))

