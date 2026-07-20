def climb_stairs(n):
    return int((((1 + 5 ** 0.5) / 2) ** (n + 1) -
                ((1 - 5 ** 0.5) / 2) ** (n + 1)) / 5 ** 0.5)


n1 = 3
print(climb_stairs(n1))
