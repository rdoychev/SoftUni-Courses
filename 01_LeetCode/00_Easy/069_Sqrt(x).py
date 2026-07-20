def my_sqrt(x):
    if x == 0:
        return 0

    low = 0
    high = x
    while low <= high:
        mid = low + (high - low) // 2
        square = mid * mid
        if square == x:
            return mid
        elif square <= x:
            low = mid + 1  # Try for a bigger answer
        else:
            high = mid - 1  # Try for a smaller answer
    return high



a = 9
print(my_sqrt(a))