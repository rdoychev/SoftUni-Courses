def can_see_stage(seats: list) -> bool:
    num_row = len(seats)
    num_col = len(seats[0])

    for col in range(num_col):
        for row in range(num_row - 1):
            if seats[row][col] < seats[row + 1][col]:
                continue
            else:
                return False
    return True


inp = [[1, 2, 3, 2, 1, 1],
       [2, 4, 4, 3, 2, 2],
       [5, 5, 5, 5, 4, 4],
       [6, 6, 7, 6, 5, 5]]

print(can_see_stage(inp))
