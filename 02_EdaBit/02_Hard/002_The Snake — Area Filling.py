def snake_fill(n: int) -> int:
    count = 0
    n = n ** 2
    while n >= 2:
        count += 1
        n = n // 2
    return count


m = snake_fill(24)
print(m)
