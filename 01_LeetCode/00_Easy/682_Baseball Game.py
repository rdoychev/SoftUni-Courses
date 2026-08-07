def cal_points(operations: list[str]) -> int:
    points = []

    for operation in operations:
        if operation == '+':
            points.append(points[-1] + points[-2])
        elif operation == 'D':
            points.append(points[-1] * 2)
        elif operation == 'C':
            points.pop()
        else:
            points.append(int(operation))

    return sum(points)


ops1 = ["1","C"]
print(cal_points(ops1))