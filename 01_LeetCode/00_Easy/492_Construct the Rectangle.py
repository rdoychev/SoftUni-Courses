def construct_rectangle(area: int) -> list:
    n = int(area ** 0.5)

    for w in range(n, 0, -1):
        if area % w == 0:
            return [area // w, w]


area1 = 4
print(construct_rectangle(area1))