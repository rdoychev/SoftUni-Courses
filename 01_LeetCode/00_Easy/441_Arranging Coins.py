def arrange_coins(n: int) -> int:
    return int(((8 * n + 1) ** 0.5 - 1) / 2)


n1 = 8
print(arrange_coins(n1))