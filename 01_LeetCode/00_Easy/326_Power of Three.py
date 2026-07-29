def is_power_of_three(n: int) -> bool:
    return n > 0 and 1162261467 % n == 0


n1 = -1
print(is_power_of_three(n1))
