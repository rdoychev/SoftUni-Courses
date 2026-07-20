def plus_one(digits: list) -> list:
    n = len(digits)
    for idx in range(n - 1, -1, -1):
        if digits[idx] < 9:
            digits[idx] += 1
            return digits
        else:
            digits[idx] = 0
    return [1] + digits


digits1 = [9,9,9,8]
print(plus_one(digits1))

