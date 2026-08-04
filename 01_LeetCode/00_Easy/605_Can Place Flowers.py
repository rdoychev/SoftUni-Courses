def can_place_flowers(flowerbed: list, n: int) -> bool:
    if n == 0:
        return True

    flowerbed = [0] + flowerbed + [0]

    count = 0
    idx = 1
    while idx < len(flowerbed) - 2:
        if flowerbed[idx] == 1:
            idx += 2
        elif flowerbed[idx - 1] == 0 and flowerbed[idx] == 0 and flowerbed[idx + 1] == 0:
            count += 1
            flowerbed[idx] = 1
            idx += 1
        else:
            idx += 1

    if flowerbed[-3] == 0 and flowerbed[-2] == 0 and flowerbed[-1] == 0:
        count += 1

    return count >= n


flowerbed1 = [1]
n1 = 1
print(can_place_flowers(flowerbed1, n1))
