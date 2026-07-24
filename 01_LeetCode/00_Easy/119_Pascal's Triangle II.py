def getRow(rowIndex):
    # if rowIndex == 0:
    #     triangle_row = [1]
    # elif rowIndex == 1:
    #     triangle_row = [1, 1]
    # else:
    #     triangle_row = [1, 1]
    #     for i in range(2, rowIndex + 1):
    #         triangle_row = [x + y for x, y in zip(([0] + triangle_row), (triangle_row + [0]))]

    triangle_row = [1]
    prev_val = 1
    for i in range(1, rowIndex + 1):
        next_val = prev_val * (rowIndex - i + 1) // i
        triangle_row.append(next_val)
        prev_val = next_val

    return triangle_row


rowIndex1 = 4
x1 = getRow(rowIndex1)
print(x1)
