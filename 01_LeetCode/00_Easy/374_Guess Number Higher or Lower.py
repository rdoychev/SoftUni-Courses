def guess_number(n: int) -> int:
    low = 1
    high = n

    while low <= high:
        mid = low + (high - low) // 2
        guess_n = guess(mid)
        print(guess_n, low, high, mid)

        if guess_n == 0:
            return mid

        elif guess_n == 1:
            low = mid + 1

        else:
            high = mid - 1

def guess(num: int) -> int:
    if num == pick:
        return 0
    elif num > pick:
        return -1
    else:
        return 1


n1 = 10
pick = 6
print(guess_number(n1))