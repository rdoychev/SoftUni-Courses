def is_perfect_square(num: int) -> bool:
    if num == 0:
        return True

    low = 0
    high = num
    while low <= high:
        mid = low + (high - low) // 2
        square = mid * mid
        if square == num:
            return True
        elif square <= num:
            low = mid + 1  # Try for a bigger answer
        else:
            high = mid - 1  # Try for a smaller answer

    return False


num1 = 16
print(is_perfect_square(num1))
